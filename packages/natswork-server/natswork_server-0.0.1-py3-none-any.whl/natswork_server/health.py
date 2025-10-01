import asyncio
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class HealthStatus(Enum):
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    WARNING = "warning"
    UNKNOWN = "unknown"


@dataclass
class HealthCheckResult:
    name: str
    status: HealthStatus
    message: str
    details: Dict[str, Any] = None
    duration_ms: float = 0
    timestamp: datetime = None

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.utcnow()
        if self.details is None:
            self.details = {}


class HealthCheck(ABC):

    def __init__(self, name: str, timeout: float = 5.0):
        self.name = name
        self.timeout = timeout

    @abstractmethod
    async def check(self) -> HealthCheckResult:
        pass

    async def execute(self) -> HealthCheckResult:
        start_time = time.time()

        try:
            result = await asyncio.wait_for(self.check(), timeout=self.timeout)
            result.duration_ms = (time.time() - start_time) * 1000
            return result
        except asyncio.TimeoutError:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.UNHEALTHY,
                message=f"Health check timed out after {self.timeout}s",
                duration_ms=(time.time() - start_time) * 1000
            )
        except Exception as e:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.UNHEALTHY,
                message=f"Health check failed: {str(e)}",
                duration_ms=(time.time() - start_time) * 1000,
                details={"exception": type(e).__name__}
            )


class NatsHealthCheck(HealthCheck):

    def __init__(self, connection_manager, name: str = "nats_connection"):
        super().__init__(name)
        self.connection_manager = connection_manager

    async def check(self) -> HealthCheckResult:
        try:
            nc = await self.connection_manager.connect()

            if not nc.is_connected:
                return HealthCheckResult(
                    name=self.name,
                    status=HealthStatus.UNHEALTHY,
                    message="NATS connection not established",
                    details={"connected": False}
                )

            rtt = await nc.rtt()

            if rtt > 1.0:
                status = HealthStatus.WARNING
                message = f"NATS connection has high latency: {rtt:.3f}s"
            else:
                status = HealthStatus.HEALTHY
                message = "NATS connection is healthy"

            return HealthCheckResult(
                name=self.name,
                status=status,
                message=message,
                details={
                    "connected": True,
                    "rtt_seconds": rtt,
                    "server_info": nc.connected_server_version
                }
            )

        except Exception as e:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.UNHEALTHY,
                message=f"NATS health check failed: {str(e)}",
                details={"exception": type(e).__name__}
            )


class JobRegistryHealthCheck(HealthCheck):

    def __init__(self, name: str = "job_registry"):
        super().__init__(name)

    async def check(self) -> HealthCheckResult:
        from natswork_server.job import JobRegistry

        jobs = JobRegistry.list_all_jobs()
        job_count = len(jobs)

        if job_count == 0:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.WARNING,
                message="No jobs registered",
                details={"job_count": 0}
            )

        return HealthCheckResult(
            name=self.name,
            status=HealthStatus.HEALTHY,
            message=f"{job_count} jobs registered",
            details={
                "job_count": job_count,
                "jobs": list(jobs.keys())
            }
        )


class WorkerHealthCheck(HealthCheck):

    def __init__(self, worker_pool_manager, name: str = "worker_pools"):
        super().__init__(name)
        self.worker_pool_manager = worker_pool_manager

    async def check(self) -> HealthCheckResult:
        try:
            pools = self.worker_pool_manager.get_active_pools()

            if not pools:
                return HealthCheckResult(
                    name=self.name,
                    status=HealthStatus.WARNING,
                    message="No active worker pools",
                    details={"active_pools": 0}
                )

            pool_stats = {}
            total_workers = 0

            for queue_name, pool in pools.items():
                stats = pool.get_stats()
                pool_stats[queue_name] = stats
                total_workers += stats.get("worker_count", 0)

            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.HEALTHY,
                message=f"{len(pools)} pools with {total_workers} workers",
                details={
                    "active_pools": len(pools),
                    "total_workers": total_workers,
                    "pool_stats": pool_stats
                }
            )

        except Exception as e:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.UNHEALTHY,
                message=f"Worker health check failed: {str(e)}",
                details={"exception": type(e).__name__}
            )


class HealthMonitor:

    def __init__(self):
        self.health_checks: List[HealthCheck] = []
        self.last_results: Dict[str, HealthCheckResult] = {}
        self._monitoring_task: Optional[asyncio.Task] = None
        self._check_interval = 30

    def add_health_check(self, health_check: HealthCheck):
        self.health_checks.append(health_check)

    async def check_all(self) -> Dict[str, HealthCheckResult]:
        tasks = [check.execute() for check in self.health_checks]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        health_results = {}
        for i, result in enumerate(results):
            check_name = self.health_checks[i].name

            if isinstance(result, Exception):
                health_results[check_name] = HealthCheckResult(
                    name=check_name,
                    status=HealthStatus.UNHEALTHY,
                    message=f"Health check raised exception: {str(result)}",
                    details={"exception": type(result).__name__}
                )
            else:
                health_results[check_name] = result

        self.last_results = health_results
        return health_results

    def get_overall_status(self) -> HealthStatus:
        if not self.last_results:
            return HealthStatus.UNKNOWN

        statuses = [result.status for result in self.last_results.values()]

        if any(status == HealthStatus.UNHEALTHY for status in statuses):
            return HealthStatus.UNHEALTHY
        elif any(status == HealthStatus.WARNING for status in statuses):
            return HealthStatus.WARNING
        elif all(status == HealthStatus.HEALTHY for status in statuses):
            return HealthStatus.HEALTHY
        else:
            return HealthStatus.UNKNOWN

    async def start_monitoring(self):
        if self._monitoring_task and not self._monitoring_task.done():
            return

        self._monitoring_task = asyncio.create_task(self._monitoring_loop())

    async def stop_monitoring(self):
        if self._monitoring_task:
            self._monitoring_task.cancel()
            try:
                await self._monitoring_task
            except asyncio.CancelledError:
                pass

    async def _monitoring_loop(self):
        import logging
        logger = logging.getLogger("natswork.health")

        while True:
            try:
                await self.check_all()
                await asyncio.sleep(self._check_interval)
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Health monitoring error: {e}")
                await asyncio.sleep(self._check_interval)
