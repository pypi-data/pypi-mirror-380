import asyncio

import pytest

from natswork_server.timeout_handler import TimeoutHandler


@pytest.mark.asyncio
async def test_execute_with_timeout_success():
    handler = TimeoutHandler()

    async def quick_task():
        await asyncio.sleep(0.01)
        return "success"

    result = await handler.execute_with_timeout("job-1", quick_task(), timeout=1.0)
    assert result == "success"
    assert "job-1" not in handler.get_active_jobs()


@pytest.mark.asyncio
async def test_execute_with_timeout_timeout():
    handler = TimeoutHandler()

    async def slow_task():
        await asyncio.sleep(10)
        return "should_not_complete"

    with pytest.raises(asyncio.TimeoutError):
        await handler.execute_with_timeout("job-2", slow_task(), timeout=0.1)

    assert "job-2" not in handler.get_active_jobs()


@pytest.mark.asyncio
async def test_cancel_job():
    handler = TimeoutHandler()

    async def long_task():
        await asyncio.sleep(10)
        return "done"

    task = asyncio.create_task(handler.execute_with_timeout("job-3", long_task(), timeout=60))

    await asyncio.sleep(0.01)

    assert "job-3" in handler.get_active_jobs()

    cancelled = handler.cancel_job("job-3")
    assert cancelled

    with pytest.raises((asyncio.TimeoutError, asyncio.CancelledError)):
        await task


@pytest.mark.asyncio
async def test_cancel_nonexistent_job():
    handler = TimeoutHandler()
    result = handler.cancel_job("nonexistent")
    assert not result


@pytest.mark.asyncio
async def test_get_active_jobs():
    handler = TimeoutHandler()

    async def task1():
        await asyncio.sleep(0.5)
        return "task1"

    async def task2():
        await asyncio.sleep(0.5)
        return "task2"

    t1 = asyncio.create_task(handler.execute_with_timeout("job-a", task1(), timeout=10))
    t2 = asyncio.create_task(handler.execute_with_timeout("job-b", task2(), timeout=10))

    await asyncio.sleep(0.01)

    active = handler.get_active_jobs()
    assert "job-a" in active
    assert "job-b" in active

    await t1
    await t2

    assert handler.get_active_jobs() == []
