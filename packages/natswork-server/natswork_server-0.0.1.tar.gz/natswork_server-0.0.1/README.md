# NatsWork Server (Python)

Server library for the NatsWork job processing system.

## Installation

```bash
pip install -e .
```

## Development

```bash
# Install with development dependencies
pip install -e ".[dev,test]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=src --cov-report=html

# Format code
black src tests

# Lint code
ruff src tests

# Type check
mypy src
```

## Status

⚠️ **Under Development** - Implementation pending (see docs/python/001-010.md)

This package provides the foundation for:
- Job processing workers
- Queue management
- Multi-threaded job execution
- Health monitoring and metrics
- Framework integration (Django, Flask, FastAPI)

## Usage

```python
from natswork_server import job, NatsWorkServer

# Define a job
@job(queue="default", retries=3)
class MyJob:
    def perform(self, x, y):
        return x + y

# Start server
server = NatsWorkServer("nats://localhost:4222")
# Coming in Tasks 004-006
```

## CLI

```bash
# Start worker server
natswork-server start --queues default --concurrency 10
```