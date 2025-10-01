"""Worker pool management for NatsWork."""

import asyncio
import logging
import threading
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Set

from .job import JobRegistry
from .messages import JobMessage, MessageBuilder, MessageSerializer
from .nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


@dataclass
class JobExecution:
    """Context for job execution"""
    job_message: JobMessage
    worker_id: str
    nats_msg: Any
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    retry_count: int = 0

    @property
    def job_id(self) -> str:
        return self.job_message.job_id

    @property
    def job_class_name(self) -> str:
        return self.job_message.job_class

    def increment_retry(self):
        self.retry_count += 1

    def get_execution_time(self) -> float:
        return (datetime.now(timezone.utc) - self.started_at).total_seconds()


@dataclass
class JobResult:
    """Result of job execution"""
    status: str
    value: Any = None
    error: Optional[Exception] = None
    execution_time: float = 0

    @classmethod
    def success(cls, value: Any = None, execution_time: float = 0) -> 'JobResult':
        return cls(status="success", value=value, execution_time=execution_time)

    @classmethod
    def from_error(cls, err: Exception, execution_time: float = 0) -> 'JobResult':
        return cls(status="error", error=err, execution_time=execution_time)

    @classmethod
    def retry(cls, error: Exception, execution_time: float = 0) -> 'JobResult':
        return cls(status="retry", error=error, execution_time=execution_time)


class WorkerPoolStats:
    """Statistics for worker pool performance"""

    def __init__(self):
        self.jobs_started = 0
        self.jobs_completed = 0
        self.jobs_failed = 0
        self.jobs_retried = 0
        self.total_execution_time = 0.0
        self.start_time = datetime.now(timezone.utc)
        self._lock = threading.Lock()

    def job_started(self):
        with self._lock:
            self.jobs_started += 1

    def job_completed(self, execution_time: float = 0):
        with self._lock:
            self.jobs_completed += 1
            self.total_execution_time += execution_time

    def job_failed(self):
        with self._lock:
            self.jobs_failed += 1

    def job_retried(self):
        with self._lock:
            self.jobs_retried += 1

    def get_stats(self) -> Dict[str, Any]:
        with self._lock:
            uptime = (datetime.now(timezone.utc) - self.start_time).total_seconds()
            return {
                "jobs_started": self.jobs_started,
                "jobs_completed": self.jobs_completed,
                "jobs_failed": self.jobs_failed,
                "jobs_retried": self.jobs_retried,
                "success_rate": self.jobs_completed / max(self.jobs_started, 1) * 100,
                "average_execution_time": self.total_execution_time / max(self.jobs_completed, 1),
                "uptime_seconds": uptime,
                "throughput_per_minute": self.jobs_completed / max(uptime / 60, 1)
            }


class WorkerPoolManager:
    """Manages multiple worker pools for different queues"""

    def __init__(self, nats_client: NatsConnectionManager):
        self.nats_client = nats_client
        self._pools: Dict[str, WorkerPool] = {}
        self._shutdown_event = asyncio.Event()
        self._tasks: Set[asyncio.Task] = set()

    async def start_pool(self, queue_name: str, concurrency: int = 10):
        """Start worker pool for specific queue"""
        if queue_name in self._pools:
            logger.warning(f"Pool for {queue_name} already exists")
            return

        pool = WorkerPool(
            queue_name=queue_name,
            concurrency=concurrency,
            nats_client=self.nats_client,
            shutdown_event=self._shutdown_event
        )

        self._pools[queue_name] = pool
        task = asyncio.create_task(pool.start())
        self._tasks.add(task)

        logger.info(f"Started worker pool for {queue_name} with {concurrency} workers")

    async def stop_pool(self, queue_name: str):
        """Stop worker pool for specific queue"""
        if queue_name not in self._pools:
            return

        pool = self._pools[queue_name]
        await pool.stop()
        del self._pools[queue_name]

        logger.info(f"Stopped worker pool for {queue_name}")

    async def shutdown(self):
        """Graceful shutdown of all worker pools"""
        logger.info("Shutting down worker pools...")
        self._shutdown_event.set()

        if self._tasks:
            await asyncio.wait(self._tasks, timeout=30)

        for pool in list(self._pools.values()):
            await pool.stop()

        self._pools.clear()
        self._tasks.clear()
        logger.info("All worker pools stopped")

    def get_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get statistics for all pools"""
        return {
            queue_name: pool.get_stats()
            for queue_name, pool in self._pools.items()
        }

    def get_active_pools(self) -> Dict[str, 'WorkerPool']:
        """Get all active worker pools"""
        return dict(self._pools)


class WorkerPool:
    """Pool of workers processing jobs from a specific queue"""

    def __init__(
        self, queue_name: str, concurrency: int, nats_client: NatsConnectionManager, shutdown_event: asyncio.Event
    ):
        self.queue_name = queue_name
        self.concurrency = concurrency
        self.nats_client = nats_client
        self.shutdown_event = shutdown_event
        self._workers: List[WorkerInstance] = []
        self._worker_tasks: Set[asyncio.Task] = set()
        self._stats = WorkerPoolStats()

    async def start(self):
        """Start all workers in the pool"""
        for i in range(self.concurrency):
            worker = WorkerInstance(
                worker_id=f"{self.queue_name}-{i}",
                queue_name=self.queue_name,
                nats_client=self.nats_client,
                shutdown_event=self.shutdown_event,
                stats=self._stats
            )
            self._workers.append(worker)

            task = asyncio.create_task(worker.run())
            self._worker_tasks.add(task)

        monitor_task = asyncio.create_task(self._monitor_workers())
        self._worker_tasks.add(monitor_task)

        await self.shutdown_event.wait()

    async def stop(self):
        """Stop all workers gracefully"""
        logger.info(f"Stopping worker pool for {self.queue_name}")

        for task in self._worker_tasks:
            task.cancel()

        try:
            await asyncio.wait_for(
                asyncio.gather(*self._worker_tasks, return_exceptions=True),
                timeout=30
            )
        except asyncio.TimeoutError:
            logger.warning("Worker tasks did not complete within timeout")

        self._worker_tasks.clear()
        self._workers.clear()

    async def _monitor_workers(self):
        """Monitor worker health and restart failed workers"""
        while not self.shutdown_event.is_set():
            try:
                await asyncio.sleep(10)
            except asyncio.CancelledError:
                break

    def get_stats(self) -> Dict[str, Any]:
        """Get pool statistics"""
        stats = self._stats.get_stats()
        stats["worker_count"] = len(self._workers)
        stats["queue_name"] = self.queue_name
        return stats


class WorkerInstance:
    """Individual worker that processes jobs from NATS"""

    def __init__(
        self,
        worker_id: str,
        queue_name: str,
        nats_client: NatsConnectionManager,
        shutdown_event: asyncio.Event,
        stats: WorkerPoolStats,
    ):
        self.worker_id = worker_id
        self.queue_name = queue_name
        self.nats_client = nats_client
        self.shutdown_event = shutdown_event
        self.stats = stats
        self._current_job: Optional[JobExecution] = None

    async def run(self):
        """Main worker loop"""
        logger.info(f"Worker {self.worker_id} started")

        try:
            nc = await self.nats_client.connect()
            js = nc.jetstream()

            subject = f"natswork.jobs.{self.queue_name}"
            psub = await js.pull_subscribe(subject, durable=f"worker-{self.worker_id}")

            while not self.shutdown_event.is_set():
                try:
                    msgs = await psub.fetch(1, timeout=1.0)

                    for msg in msgs:
                        if self.shutdown_event.is_set():
                            break

                        await self._process_job_message(msg)

                except asyncio.TimeoutError:
                    continue
                except Exception as e:
                    logger.error(f"Worker {self.worker_id} error: {e}")
                    await asyncio.sleep(1)

        except asyncio.CancelledError:
            logger.info(f"Worker {self.worker_id} cancelled")
        except Exception as e:
            logger.error(f"Worker {self.worker_id} failed: {e}")
        finally:
            logger.info(f"Worker {self.worker_id} stopped")

    async def _process_job_message(self, msg):
        """Process a single job message"""
        execution = None
        try:
            job_message = MessageSerializer.deserialize(msg.data, JobMessage)

            execution = JobExecution(
                job_message=job_message,
                worker_id=self.worker_id,
                nats_msg=msg
            )

            self._current_job = execution
            self.stats.job_started()

            from .job_executor import JobExecutor
            executor = JobExecutor()
            result = await executor.execute_job(execution)

            await self._send_job_result(execution, result)
            await msg.ack()

            self.stats.job_completed(execution.get_execution_time())
            logger.info(f"Job {execution.job_id} completed by {self.worker_id}")

        except Exception as e:
            if execution:
                await self._handle_job_error(execution, e)
            else:
                logger.error(f"Failed to process message: {e}")
                await msg.nak()
        finally:
            self._current_job = None

    async def _send_job_result(self, execution: JobExecution, result: JobResult):
        """Send job result back via NATS"""
        result_message = MessageBuilder.build_result_message(
            job_id=execution.job_id,
            status=result.status,
            result=result.value,
            error=result.error,
            processing_time=result.execution_time
        )

        result_data = MessageSerializer.serialize(result_message)

        nc = await self.nats_client.connect()
        result_subject = f"natswork.results.{execution.job_message.queue}"
        await nc.publish(result_subject, result_data)

    async def _handle_job_error(self, execution: JobExecution, error: Exception):
        """Handle job execution error with retry logic"""
        execution.increment_retry()
        self.stats.job_failed()

        job_config = JobRegistry.get_job_config(execution.job_message.job_class)

        if job_config and execution.retry_count < job_config.retries:
            await self._schedule_retry(execution, error)
            await execution.nats_msg.ack()
            self.stats.job_retried()
        else:
            result = JobResult.from_error(error, execution.get_execution_time())
            await self._send_job_result(execution, result)
            await execution.nats_msg.ack()

        logger.error(f"Job {execution.job_id} failed: {error}")

    async def _schedule_retry(self, execution: JobExecution, error: Exception):
        """Schedule job retry with delay"""
        job_config = JobRegistry.get_job_config(execution.job_message.job_class)
        delay = job_config.calculate_retry_delay(execution.retry_count) if job_config else 5

        execution.job_message.retry_count = execution.retry_count

        retry_data = MessageSerializer.serialize(execution.job_message)

        nc = await self.nats_client.connect()
        js = nc.jetstream()

        await asyncio.sleep(delay)
        await js.publish(f"natswork.jobs.{execution.job_message.queue}", retry_data)

        logger.info(f"Scheduled retry {execution.retry_count} for job {execution.job_id} in {delay}s")
