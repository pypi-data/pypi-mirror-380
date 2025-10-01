"""Job status tracking for NatsWork server-side"""
import asyncio
import json
import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, Optional

from .nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


class JobStatus(Enum):
    """Job execution status"""
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    RETRYING = "retrying"


@dataclass
class JobStatusInfo:
    """Detailed job status information"""
    job_id: str
    status: JobStatus
    job_class: str
    queue: str
    worker_id: Optional[str] = None
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    retry_count: int = 0
    error: Optional[str] = None
    progress: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization"""
        return {
            "job_id": self.job_id,
            "status": self.status.value,
            "job_class": self.job_class,
            "queue": self.queue,
            "worker_id": self.worker_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "retry_count": self.retry_count,
            "error": self.error,
            "progress": self.progress
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'JobStatusInfo':
        """Create from dictionary"""
        return cls(
            job_id=data["job_id"],
            status=JobStatus(data["status"]),
            job_class=data["job_class"],
            queue=data["queue"],
            worker_id=data.get("worker_id"),
            created_at=(
                datetime.fromisoformat(data["created_at"]) if data.get("created_at") else datetime.now(timezone.utc)
            ),
            started_at=datetime.fromisoformat(data["started_at"]) if data.get("started_at") else None,
            completed_at=datetime.fromisoformat(data["completed_at"]) if data.get("completed_at") else None,
            retry_count=data.get("retry_count", 0),
            error=data.get("error"),
            progress=data.get("progress", {})
        )


class JobStatusTracker:
    """Tracks job status on the server side"""

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager
        self._status_cache: Dict[str, JobStatusInfo] = {}
        self._subscription_task: Optional[asyncio.Task] = None
        self._running = False

    async def start(self):
        """Start status tracking"""
        if self._running:
            return

        self._running = True

        # Subscribe to status requests
        nc = await self.connection_manager.connect()
        await nc.subscribe("natswork.status.*", cb=self._handle_status_request)

        logger.info("Job status tracker started")

    async def stop(self):
        """Stop status tracking"""
        self._running = False
        if self._subscription_task:
            self._subscription_task.cancel()
            try:
                await self._subscription_task
            except asyncio.CancelledError:
                pass

        logger.info("Job status tracker stopped")

    async def update_status(self, status_info: JobStatusInfo):
        """Update job status"""
        self._status_cache[status_info.job_id] = status_info

        # Publish status update
        nc = await self.connection_manager.connect()
        status_subject = f"natswork.status.updates.{status_info.job_id}"
        status_data = json.dumps(status_info.to_dict()).encode()

        try:
            await nc.publish(status_subject, status_data)
        except Exception as e:
            logger.error(f"Failed to publish status update: {e}")

    async def track_job_started(self, job_id: str, job_class: str, queue: str, worker_id: str):
        """Track when a job starts execution"""
        status_info = self._status_cache.get(job_id)

        if status_info:
            status_info.status = JobStatus.RUNNING
            status_info.started_at = datetime.now(timezone.utc)
            status_info.worker_id = worker_id
        else:
            status_info = JobStatusInfo(
                job_id=job_id,
                status=JobStatus.RUNNING,
                job_class=job_class,
                queue=queue,
                worker_id=worker_id,
                started_at=datetime.now(timezone.utc)
            )

        await self.update_status(status_info)

    async def track_job_completed(self, job_id: str, success: bool = True, error: str = None):
        """Track when a job completes"""
        status_info = self._status_cache.get(job_id)

        if not status_info:
            logger.warning(f"Cannot track completion for unknown job {job_id}")
            return

        status_info.status = JobStatus.COMPLETED if success else JobStatus.FAILED
        status_info.completed_at = datetime.now(timezone.utc)
        if error:
            status_info.error = error

        await self.update_status(status_info)

        # Clean up from cache after some time
        await asyncio.sleep(300)  # Keep for 5 minutes
        self._status_cache.pop(job_id, None)

    async def track_job_retry(self, job_id: str, retry_count: int, error: str = None):
        """Track when a job is being retried"""
        status_info = self._status_cache.get(job_id)

        if not status_info:
            logger.warning(f"Cannot track retry for unknown job {job_id}")
            return

        status_info.status = JobStatus.RETRYING
        status_info.retry_count = retry_count
        if error:
            status_info.error = error

        await self.update_status(status_info)

    def get_status(self, job_id: str) -> Optional[JobStatusInfo]:
        """Get current status of a job"""
        return self._status_cache.get(job_id)

    async def _handle_status_request(self, msg):
        """Handle status request from client"""
        try:
            # Extract job_id from subject (natswork.status.{job_id})
            subject_parts = msg.subject.split(".")
            if len(subject_parts) < 3:
                return

            job_id = subject_parts[2]
            status_info = self.get_status(job_id)

            if status_info:
                response_data = json.dumps(status_info.to_dict()).encode()
            else:
                response_data = json.dumps({"error": "Job not found"}).encode()

            if msg.reply:
                nc = await self.connection_manager.connect()
                await nc.publish(msg.reply, response_data)

        except Exception as e:
            logger.error(f"Error handling status request: {e}")


# Global status tracker instance
_status_tracker: Optional[JobStatusTracker] = None


def get_status_tracker() -> Optional[JobStatusTracker]:
    """Get global status tracker instance"""
    return _status_tracker


def set_status_tracker(tracker: JobStatusTracker):
    """Set global status tracker instance"""
    global _status_tracker
    _status_tracker = tracker
