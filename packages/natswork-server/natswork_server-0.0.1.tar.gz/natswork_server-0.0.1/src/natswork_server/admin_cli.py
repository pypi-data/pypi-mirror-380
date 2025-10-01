import asyncio

import click

from natswork_server.dlq import DeadLetterQueueManager
from natswork_server.job import JobRegistry
from natswork_server.nats_client import NatsConnectionManager


@click.group()
def admin():
    pass


@admin.group()
def dlq():
    pass


@dlq.command()
@click.option('--queue', required=True, help='Queue name')
@click.option('--limit', default=10, help='Number of messages to show')
@click.option('--servers', default='nats://localhost:4222', help='NATS servers')
def list_messages(queue, limit, servers):
    asyncio.run(_list_dlq_messages(queue, limit, servers.split(',')))


async def _list_dlq_messages(queue: str, limit: int, servers: list):
    connection_manager = NatsConnectionManager(servers)
    await connection_manager.connect()

    dlq_manager = DeadLetterQueueManager(connection_manager)

    try:
        messages = await dlq_manager.list_dlq_messages(queue, limit)

        if not messages:
            click.echo(f"No messages in DLQ for queue '{queue}'")
            return

        click.echo(f"Dead Letter Queue Messages for '{queue}':")
        click.echo("-" * 60)

        for msg in messages:
            click.echo(f"Job ID: {msg.original_job.job_id}")
            click.echo(f"Job Class: {msg.original_job.job_class}")
            click.echo(f"Failure Count: {msg.failure_count}")
            click.echo(f"Last Failed: {msg.last_failed_at}")
            click.echo(f"Reason: {msg.failure_reason}")
            click.echo("-" * 60)

    finally:
        await connection_manager.disconnect()


@dlq.command()
@click.option('--queue', required=True, help='Queue name')
@click.option('--job-id', help='Specific job ID to requeue')
@click.option('--servers', default='nats://localhost:4222', help='NATS servers')
def requeue(queue, job_id, servers):
    asyncio.run(_requeue_dlq_messages(queue, job_id, servers.split(',')))


async def _requeue_dlq_messages(queue: str, job_id: str, servers: list):
    connection_manager = NatsConnectionManager(servers)
    await connection_manager.connect()

    dlq_manager = DeadLetterQueueManager(connection_manager)

    try:
        messages = await dlq_manager.list_dlq_messages(queue, 1000)

        if job_id:
            messages = [msg for msg in messages if msg.original_job.job_id == job_id]

        if not messages:
            click.echo("No messages to requeue")
            return

        requeued_count = 0
        for msg in messages:
            if await dlq_manager.requeue_message(msg):
                requeued_count += 1
                click.echo(f"Requeued job {msg.original_job.job_id}")

        click.echo(f"Requeued {requeued_count} messages")

    finally:
        await connection_manager.disconnect()


@admin.command()
def jobs():
    jobs_dict = JobRegistry.list_all_jobs()

    if not jobs_dict:
        click.echo("No jobs registered")
        return

    click.echo("Registered Jobs:")
    click.echo("-" * 80)

    for job_name, config in jobs_dict.items():
        click.echo(f"Job: {job_name}")
        click.echo(f"  Queue: {config.queue}")
        click.echo(f"  Retries: {config.retries}")
        click.echo(f"  Timeout: {config.timeout}s")
        click.echo(f"  Priority: {config.priority}")
        click.echo()


@admin.command()
@click.option('--servers', default='nats://localhost:4222', help='NATS servers')
def status(servers):
    asyncio.run(_show_status(servers.split(',')))


async def _show_status(servers: list):
    from natswork_server.health import (
        HealthMonitor,
        JobRegistryHealthCheck,
        NatsHealthCheck,
    )

    connection_manager = NatsConnectionManager(servers)
    health_monitor = HealthMonitor()

    health_monitor.add_health_check(NatsHealthCheck(connection_manager))
    health_monitor.add_health_check(JobRegistryHealthCheck())

    results = await health_monitor.check_all()
    overall_status = health_monitor.get_overall_status()

    click.echo("System Status:")
    click.echo("=" * 50)
    click.echo(f"Overall Status: {overall_status.value.upper()}")
    click.echo()

    for name, result in results.items():
        status_color = "green" if result.status.value == "healthy" else "red"
        click.echo(f"{name}: ", nl=False)
        click.secho(result.status.value.upper(), fg=status_color)
        click.echo(f"  Message: {result.message}")
        click.echo(f"  Duration: {result.duration_ms:.1f}ms")
        click.echo()

    await connection_manager.disconnect()


if __name__ == '__main__':
    admin()
