"""Pytest configuration and fixtures for natswork-client tests."""

import asyncio

import pytest

# Pytest configuration
pytest_plugins = ["pytest_asyncio"]


@pytest.fixture(scope="session")
def event_loop():
    """Create an event loop for the test session."""
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def nats_url() -> str:
    """NATS server URL for testing."""
    return "nats://localhost:4222"


@pytest.fixture
def mock_job_data() -> dict:
    """Sample job data for testing."""
    return {
        "job_id": "test-job-123",
        "job_class": "TestJob",
        "arguments": [1, 2, 3],
        "queue": "default",
        "created_at": "2023-01-01T00:00:00Z"
    }
