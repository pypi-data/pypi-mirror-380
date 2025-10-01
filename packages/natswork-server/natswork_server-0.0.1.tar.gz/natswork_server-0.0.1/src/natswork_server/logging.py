import json
import logging
import sys
from contextlib import contextmanager
from datetime import datetime
from typing import Optional


class StructuredFormatter(logging.Formatter):

    def __init__(self, service_name: str = "natswork"):
        self.service_name = service_name
        super().__init__()

    def format(self, record: logging.LogRecord) -> str:
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "service": self.service_name,
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
        }

        if hasattr(record, 'job_id'):
            log_entry["job_id"] = record.job_id
        if hasattr(record, 'worker_id'):
            log_entry["worker_id"] = record.worker_id
        if hasattr(record, 'queue'):
            log_entry["queue"] = record.queue
        if hasattr(record, 'execution_time'):
            log_entry["execution_time"] = record.execution_time

        if record.exc_info:
            log_entry["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": self.formatException(record.exc_info)
            }

        return json.dumps(log_entry)


class NatsWorkLogger:

    @staticmethod
    def configure_logging(
        level: str = "INFO",
        format_type: str = "structured",
        output: str = "stdout"
    ):
        logger = logging.getLogger("natswork")
        logger.setLevel(getattr(logging, level.upper()))

        if output == "stdout":
            handler = logging.StreamHandler(sys.stdout)
        elif output == "stderr":
            handler = logging.StreamHandler(sys.stderr)
        else:
            handler = logging.FileHandler(output)

        if format_type == "structured":
            formatter = StructuredFormatter()
        else:
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger


@contextmanager
def job_logging_context(job_id: str, worker_id: Optional[str] = None, queue: Optional[str] = None):

    class JobLoggerAdapter(logging.LoggerAdapter):
        def process(self, msg, kwargs):
            extra = kwargs.get('extra', {})
            extra.update({
                'job_id': job_id,
                'worker_id': worker_id,
                'queue': queue
            })
            kwargs['extra'] = extra
            return msg, kwargs

    logger = logging.getLogger("natswork")
    job_logger = JobLoggerAdapter(logger, {})

    yield job_logger
