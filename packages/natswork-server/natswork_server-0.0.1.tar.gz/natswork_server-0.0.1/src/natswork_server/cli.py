"""NatsWork server CLI."""

import asyncio

import click

from .server import NatsWorkServer


@click.group()
def main():
    """NatsWork Server CLI."""
    pass


@main.command()
@click.option("--queues", "-q", multiple=True, default=["default"], help="Queues to process")
@click.option("--concurrency", "-c", default=10, help="Number of concurrent jobs")
@click.option("--nats-url", default="nats://localhost:4222", help="NATS server URL")
def start(queues, concurrency, nats_url):
    """Start the NatsWork server."""
    click.echo(f"Starting NatsWork server with queues: {list(queues)}")

    server = NatsWorkServer(
        queues=list(queues),
        concurrency=concurrency,
        nats_url=nats_url
    )

    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        click.echo("Shutting down...")


if __name__ == "__main__":
    main()
