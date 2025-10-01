from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict


@dataclass
class JobContext:
    job_id: str
    worker_id: str
    queue: str
    retry_count: int
    created_at: datetime
    started_at: datetime
    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_metadata(self, key: str, value: Any):
        self.metadata[key] = value

    def get_metadata(self, key: str, default=None):
        return self.metadata.get(key, default)

    def get_execution_time(self) -> float:
        return (datetime.now(timezone.utc) - self.started_at).total_seconds()

    def is_retry(self) -> bool:
        return self.retry_count > 0
