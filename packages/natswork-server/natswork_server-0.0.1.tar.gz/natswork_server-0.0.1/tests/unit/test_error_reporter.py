import uuid
from datetime import datetime, timezone
from unittest.mock import MagicMock

import pytest

from natswork_server.error_reporter import JobErrorReporter
from natswork_server.messages import JobMessage
from natswork_server.worker_pool import JobExecution


@pytest.fixture
def job_execution():
    job_message = JobMessage(
        job_id=str(uuid.uuid4()),
        job_class="TestJob",
        arguments={},
        queue="default",
        created_at=datetime.now(timezone.utc)
    )
    return JobExecution(
        job_message=job_message,
        worker_id="worker-1",
        nats_msg=MagicMock()
    )


@pytest.mark.asyncio
async def test_report_error_with_sync_handler(job_execution):
    reporter = JobErrorReporter()
    called_with = None

    def sync_handler(error_info):
        nonlocal called_with
        called_with = error_info

    reporter.add_error_handler(sync_handler)

    error = ValueError("test error")
    await reporter.report_error(job_execution, error)

    assert called_with is not None
    assert "job_id" in called_with
    assert called_with["error_type"] == "ValueError"
    assert called_with["error_message"] == "test error"


@pytest.mark.asyncio
async def test_report_error_with_async_handler(job_execution):
    reporter = JobErrorReporter()
    called_with = None

    async def async_handler(error_info):
        nonlocal called_with
        called_with = error_info

    reporter.add_error_handler(async_handler)

    error = RuntimeError("async test error")
    await reporter.report_error(job_execution, error)

    assert called_with is not None
    assert "job_id" in called_with
    assert called_with["error_type"] == "RuntimeError"
    assert called_with["error_message"] == "async test error"


@pytest.mark.asyncio
async def test_report_error_with_multiple_handlers(job_execution):
    reporter = JobErrorReporter()
    call_count = 0

    def handler1(error_info):
        nonlocal call_count
        call_count += 1

    async def handler2(error_info):
        nonlocal call_count
        call_count += 1

    reporter.add_error_handler(handler1)
    reporter.add_error_handler(handler2)

    error = Exception("multi handler test")
    await reporter.report_error(job_execution, error)

    assert call_count == 2


@pytest.mark.asyncio
async def test_report_error_with_context(job_execution):
    reporter = JobErrorReporter()
    received_context = None

    def handler(error_info):
        nonlocal received_context
        received_context = error_info["context"]

    reporter.add_error_handler(handler)

    error = Exception("context test")
    context = {"custom_data": "test_value"}
    await reporter.report_error(job_execution, error, context)

    assert received_context == context


@pytest.mark.asyncio
async def test_handler_error_does_not_propagate(job_execution):
    reporter = JobErrorReporter()

    def failing_handler(error_info):
        raise Exception("handler error")

    def working_handler(error_info):
        pass

    reporter.add_error_handler(failing_handler)
    reporter.add_error_handler(working_handler)

    error = Exception("test")

    await reporter.report_error(job_execution, error)
