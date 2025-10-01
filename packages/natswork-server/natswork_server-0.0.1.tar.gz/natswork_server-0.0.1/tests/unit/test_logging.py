import json
import logging

from natswork_server.logging import (
    NatsWorkLogger,
    StructuredFormatter,
    job_logging_context,
)


def test_structured_formatter():
    formatter = StructuredFormatter(service_name="test-service")

    record = logging.LogRecord(
        name="test",
        level=logging.INFO,
        pathname="test.py",
        lineno=10,
        msg="Test message",
        args=(),
        exc_info=None
    )
    record.job_id = "job-123"
    record.worker_id = "worker-1"

    output = formatter.format(record)
    parsed = json.loads(output)

    assert parsed["service"] == "test-service"
    assert parsed["level"] == "INFO"
    assert parsed["message"] == "Test message"
    assert parsed["job_id"] == "job-123"
    assert parsed["worker_id"] == "worker-1"


def test_natswork_logger_configuration():
    logger = NatsWorkLogger.configure_logging(level="DEBUG", format_type="simple")

    assert logger.name == "natswork"
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) > 0


def test_job_logging_context():
    with job_logging_context(job_id="job-123", worker_id="worker-1", queue="default") as logger:
        assert isinstance(logger, logging.LoggerAdapter)
