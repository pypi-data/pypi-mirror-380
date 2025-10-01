# NatsWork Client (Python)

Client library for the NatsWork job processing system.

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
- Job dispatching to NATS queues
- Synchronous and asynchronous job execution
- Result handling and status tracking
- Cross-language protocol compatibility

## Usage

```python
from natswork_client import NatsWorkClient

# Coming in Task 007 - Client Interface
client = NatsWorkClient("nats://localhost:4222")
```