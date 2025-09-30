import asyncio
import signal
import time
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional

from aio_pika.abc import AbstractIncomingMessage

from llmq.core.config import get_config
from llmq.core.broker import BrokerManager
from llmq.core.models import Job, Result


class BaseWorker(ABC):
    """Abstract base class for all worker implementations."""

    def __init__(
        self,
        queue_name: str,
        worker_id: Optional[str] = None,
        concurrency: Optional[int] = None,
        pipeline_name: Optional[str] = None,
        stage_name: Optional[str] = None,
        pipeline_stages: Optional[list[str]] = None,
    ):
        self.queue_name = queue_name
        self.worker_id = worker_id or self._generate_worker_id()
        self.config = get_config()
        self.concurrency = concurrency  # Override prefetch if specified

        # Pipeline configuration
        self.pipeline_name = pipeline_name
        self.stage_name = stage_name
        self.pipeline_stages = pipeline_stages
        self.is_pipeline_worker = pipeline_name is not None and stage_name is not None

        # Set up structured logging for workers
        from llmq.utils.logging import setup_logging

        self.logger = setup_logging(f"llmq.worker.{self.worker_id}", structured=True)

        self.broker: Optional[BrokerManager] = None
        self.running = False
        self.jobs_processed = 0
        self.total_duration_ms = 0.0

        # Set up graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)

    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully."""
        self.logger.info(f"Received signal {signum}, shutting down gracefully...")
        self.running = False

    @abstractmethod
    def _generate_worker_id(self) -> str:
        """Generate a unique worker ID for this worker type."""
        pass

    @abstractmethod
    async def _initialize_processor(self) -> None:
        """Initialize the processing engine (vLLM, dummy, etc.)."""
        pass

    @abstractmethod
    async def _process_job(self, job: Job) -> str:
        """Process a single job and return the result text."""
        pass

    @abstractmethod
    async def _cleanup_processor(self) -> None:
        """Clean up processing resources."""
        pass

    async def initialize(self) -> None:
        """Initialize worker components."""
        if self.is_pipeline_worker:
            self.logger.info(
                f"Initializing pipeline worker {self.worker_id} for stage {self.stage_name}"
            )
        else:
            self.logger.info(f"Initializing worker {self.worker_id}")

        # Initialize processing engine
        await self._initialize_processor()

        # Initialize RabbitMQ connection
        self.broker = BrokerManager(self.config)
        await self.broker.connect()

        # Override prefetch if concurrency is specified
        if self.concurrency is not None and self.broker.channel is not None:
            await self.broker.channel.set_qos(prefetch_count=self.concurrency)
            self.logger.info(f"Set concurrency to {self.concurrency} jobs")

        # Set up queue infrastructure
        if self.is_pipeline_worker:
            # Pipeline worker: need to know stage order for routing
            # For now, we'll get this from pipeline config when needed
            # Set up queue infrastructure for this stage
            await self.broker.setup_queue_infrastructure(self.queue_name)

            self.logger.info(
                f"Connected to pipeline {self.pipeline_name}, stage {self.stage_name}"
            )
        else:
            # Regular worker: set up standard infrastructure
            await self.broker.setup_queue_infrastructure(self.queue_name)

        self.logger.info("Worker initialization complete")

    async def run(self) -> None:
        """Main worker loop."""
        try:
            await self.initialize()
            self.running = True

            self.logger.info(
                f"Worker {self.worker_id} starting to consume from queue {self.queue_name}"
            )

            # Start consuming jobs
            if self.broker is not None:
                await self.broker.consume_jobs(self.queue_name, self._process_message)

            # Keep the worker running
            while self.running:
                await asyncio.sleep(1)

        except Exception as e:
            self.logger.error(f"Worker error: {e}", exc_info=True)
        finally:
            await self.cleanup()

    async def _process_message(self, message: AbstractIncomingMessage) -> None:
        """Process a single job message."""
        start_time = time.time()
        job_id = None

        try:
            # Parse job
            job = Job.parse_raw(message.body)
            job_id = job.id

            self.logger.info(f"Processing job {job_id}")

            # Process job using implementation-specific method
            result_text = await self._process_job(job)

            # Calculate duration
            duration_ms = (time.time() - start_time) * 1000

            # Get prompt for result logging
            if job.messages:
                # For chat jobs, create a summary of messages
                prompt_for_result = f"Chat with {len(job.messages)} messages"
            else:
                # For regular jobs, use formatted prompt
                prompt_for_result = job.get_formatted_prompt()

            # Create result with required fields
            result = Result(
                id=job_id,
                prompt=prompt_for_result,
                result=result_text,
                worker_id=self.worker_id,
                duration_ms=duration_ms,
                timestamp=datetime.utcnow(),
            )

            # Preserve custom fields from original job (like url, fineweb_id)
            job_dict = job.model_dump()
            for key, value in job_dict.items():
                if key not in [
                    "id",
                    "prompt",
                    "messages",
                    "chat_mode",
                    "result",
                    "worker_id",
                    "duration_ms",
                    "timestamp",
                ]:
                    setattr(result, key, value)

            # Publish result
            if self.broker is not None:
                if self.is_pipeline_worker:
                    # Pipeline worker: route result to next stage or final results
                    if self.pipeline_name is None or self.stage_name is None:
                        raise RuntimeError(
                            "Pipeline worker missing pipeline_name or stage_name"
                        )

                    # Get pipeline stages if not already loaded
                    if self.pipeline_stages is None:
                        self.pipeline_stages = await self._get_pipeline_stages()

                    await self.broker.publish_pipeline_result(
                        self.pipeline_name,
                        self.stage_name,
                        self.pipeline_stages,
                        result,
                    )
                else:
                    # Regular worker: publish to results queue
                    await self.broker.publish_result(self.queue_name, result)

            # Acknowledge message
            await message.ack()

            # Update stats
            self.jobs_processed += 1
            self.total_duration_ms += duration_ms

            self.logger.info(
                f"Completed job {job_id}",
                extra={
                    "job_id": job_id,
                    "duration_ms": duration_ms,
                    "jobs_processed": self.jobs_processed,
                    "avg_duration_ms": self.total_duration_ms / self.jobs_processed,
                },
            )

        except ValueError as e:
            # Handle ValueError specially - don't requeue, just drop the job
            self.logger.warning(
                f"Dropping job {job_id} due to ValueError (not requeuing): {e}",
                extra={"job_id": job_id, "error": str(e)},
            )
            # Acknowledge the message to remove it from queue without requeuing
            await message.ack()

        except Exception as e:
            self.logger.error(
                f"Error processing job {job_id}: {e}",
                extra={"job_id": job_id, "error": str(e)},
                exc_info=True,
            )

            # Reject message (will be requeued for retry)
            await message.reject(requeue=True)

    async def _get_pipeline_stages(self) -> list[str]:
        """Get the ordered list of stages for this pipeline."""
        if self.pipeline_stages is not None:
            return self.pipeline_stages

        # Fallback - this shouldn't happen in normal operation
        if self.pipeline_name is None:
            raise RuntimeError("Pipeline name not set")

        # For now, we'll need to infer this from the queue name pattern
        # In a more sophisticated implementation, this could be stored in Redis/etc
        # For testing purposes, we'll assume a simple pattern
        # This method should be overridden by pipeline-aware workers
        return [self.stage_name] if self.stage_name else []

    async def cleanup(self) -> None:
        """Clean up resources."""
        self.logger.info(f"Worker {self.worker_id} shutting down...")

        # Clean up processing resources
        await self._cleanup_processor()

        # Clean up broker connection
        if self.broker:
            await self.broker.disconnect()

        self.logger.info(
            f"Worker {self.worker_id} shutdown complete. Processed {self.jobs_processed} jobs."
        )
