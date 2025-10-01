import asyncio
import logging
from typing import Coroutine, Dict, List

logger = logging.getLogger(__name__)


class TimeoutHandler:

    def __init__(self):
        self._active_jobs: Dict[str, asyncio.Task] = {}

    async def execute_with_timeout(self, job_id: str, coro: Coroutine, timeout: float):
        task = asyncio.create_task(coro)
        self._active_jobs[job_id] = task

        try:
            return await asyncio.wait_for(task, timeout=timeout)
        except asyncio.TimeoutError:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
            raise
        finally:
            self._active_jobs.pop(job_id, None)

    def cancel_job(self, job_id: str) -> bool:
        task = self._active_jobs.get(job_id)
        if task and not task.done():
            task.cancel()
            return True
        return False

    def get_active_jobs(self) -> List[str]:
        return list(self._active_jobs.keys())
