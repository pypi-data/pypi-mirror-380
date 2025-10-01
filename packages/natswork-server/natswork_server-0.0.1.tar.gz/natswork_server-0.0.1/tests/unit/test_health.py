from unittest.mock import AsyncMock, MagicMock

import pytest

from natswork_server.health import (
    HealthCheck,
    HealthCheckResult,
    HealthMonitor,
    HealthStatus,
    JobRegistryHealthCheck,
    NatsHealthCheck,
)


class SimpleHealthCheck(HealthCheck):
    def __init__(self, name: str, should_pass: bool = True):
        super().__init__(name)
        self.should_pass = should_pass

    async def check(self) -> HealthCheckResult:
        if self.should_pass:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.HEALTHY,
                message="Check passed"
            )
        else:
            return HealthCheckResult(
                name=self.name,
                status=HealthStatus.UNHEALTHY,
                message="Check failed"
            )


@pytest.mark.asyncio
async def test_health_check_execute():
    check = SimpleHealthCheck("test_check", should_pass=True)
    result = await check.execute()

    assert result.status == HealthStatus.HEALTHY
    assert result.duration_ms > 0


@pytest.mark.asyncio
async def test_nats_health_check():
    mock_connection_manager = MagicMock()
    mock_nc = MagicMock()
    mock_nc.is_connected = True
    mock_nc.rtt = AsyncMock(return_value=0.05)
    mock_nc.connected_server_version = "2.9.0"

    mock_connection_manager.connect = AsyncMock(return_value=mock_nc)

    check = NatsHealthCheck(mock_connection_manager)
    result = await check.check()

    assert result.status == HealthStatus.HEALTHY
    assert result.details["connected"] is True


@pytest.mark.asyncio
async def test_job_registry_health_check():
    check = JobRegistryHealthCheck()
    result = await check.check()

    assert result.status in [HealthStatus.HEALTHY, HealthStatus.WARNING]
    assert "job_count" in result.details


@pytest.mark.asyncio
async def test_health_monitor():
    monitor = HealthMonitor()

    monitor.add_health_check(SimpleHealthCheck("check1", should_pass=True))
    monitor.add_health_check(SimpleHealthCheck("check2", should_pass=False))

    results = await monitor.check_all()

    assert len(results) == 2
    assert monitor.get_overall_status() == HealthStatus.UNHEALTHY
