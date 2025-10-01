import json
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List

from natswork_server.messages import JobMessage, MessageSerializer
from natswork_server.nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


@dataclass
class DeadLetterMessage:
    original_job: JobMessage
    failure_reason: str
    failure_count: int
    first_failed_at: datetime
    last_failed_at: datetime
    original_queue: str
    worker_id: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "original_job": self.original_job.model_dump(),
            "failure_reason": self.failure_reason,
            "failure_count": self.failure_count,
            "first_failed_at": self.first_failed_at.isoformat(),
            "last_failed_at": self.last_failed_at.isoformat(),
            "original_queue": self.original_queue,
            "worker_id": self.worker_id
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DeadLetterMessage':
        return cls(
            original_job=JobMessage(**data["original_job"]),
            failure_reason=data["failure_reason"],
            failure_count=data["failure_count"],
            first_failed_at=datetime.fromisoformat(data["first_failed_at"]),
            last_failed_at=datetime.fromisoformat(data["last_failed_at"]),
            original_queue=data["original_queue"],
            worker_id=data["worker_id"]
        )


class DeadLetterQueueManager:

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager
        self.dlq_subject_prefix = "natswork.dlq"

    async def send_to_dlq(
        self,
        job_message: JobMessage,
        failure_reason: str,
        failure_count: int,
        worker_id: str,
        original_queue: str
    ):

        dlq_message = DeadLetterMessage(
            original_job=job_message,
            failure_reason=failure_reason,
            failure_count=failure_count,
            first_failed_at=datetime.utcnow(),
            last_failed_at=datetime.utcnow(),
            original_queue=original_queue,
            worker_id=worker_id
        )

        dlq_subject = f"{self.dlq_subject_prefix}.{original_queue}"
        dlq_data = json.dumps(dlq_message.to_dict()).encode()

        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        try:
            await js.publish(dlq_subject, dlq_data)
            logger.info(
                f"Job {job_message.job_id} sent to DLQ after {failure_count} failures",
                extra={
                    "job_id": job_message.job_id,
                    "original_queue": original_queue,
                    "failure_reason": failure_reason
                }
            )
        except Exception as e:
            logger.error(f"Failed to send job to DLQ: {e}")
            raise

    async def list_dlq_messages(self, queue: str, limit: int = 100) -> List[DeadLetterMessage]:
        dlq_subject = f"{self.dlq_subject_prefix}.{queue}"

        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        try:
            consumer_config = {
                "durable_name": f"dlq_reader_{queue}",
                "deliver_policy": "all",
                "max_deliver": 1
            }

            psub = await js.pull_subscribe(dlq_subject, **consumer_config)

            messages = []
            msgs = await psub.fetch(limit, timeout=5.0)

            for msg in msgs:
                try:
                    data = json.loads(msg.data.decode())
                    dlq_message = DeadLetterMessage.from_dict(data)
                    messages.append(dlq_message)
                except Exception as e:
                    logger.warning(f"Failed to parse DLQ message: {e}")

            return messages

        except Exception as e:
            logger.error(f"Failed to list DLQ messages: {e}")
            return []

    async def requeue_message(self, dlq_message: DeadLetterMessage) -> bool:
        try:
            job_message = dlq_message.original_job
            job_message.retry_count = 0

            queue_subject = f"natswork.jobs.{dlq_message.original_queue}"
            job_data = MessageSerializer.serialize(job_message)

            nc = await self.connection_manager.connect()
            js = nc.jetstream()

            await js.publish(queue_subject, job_data)

            logger.info(
                f"Requeued job {job_message.job_id} from DLQ to {dlq_message.original_queue}",
                extra={"job_id": job_message.job_id, "queue": dlq_message.original_queue}
            )

            return True

        except Exception as e:
            logger.error(f"Failed to requeue message: {e}")
            return False

    async def purge_dlq(self, queue: str) -> int:
        try:
            nc = await self.connection_manager.connect()
            js = nc.jetstream()

            stream_name = f"DLQ_{queue.upper()}"

            try:
                await js.delete_stream(stream_name)
                logger.info(f"Purged DLQ for queue {queue}")
                return 1
            except Exception:
                return 0

        except Exception as e:
            logger.error(f"Failed to purge DLQ: {e}")
            return 0
