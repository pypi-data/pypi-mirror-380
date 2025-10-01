from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from natswork_client.async_support import AsyncJobDispatcher, natswork_client
from natswork_client.client import NatsWorkClient


@pytest.mark.asyncio
async def test_natswork_client_context_manager():
    with patch('natswork_client.async_support.NatsWorkClient') as MockClient:
        mock_instance = MockClient.return_value
        mock_instance.connect = AsyncMock()
        mock_instance.disconnect = AsyncMock()

        async with natswork_client(servers=['nats://test:4222']) as client:
            assert client == mock_instance

        mock_instance.connect.assert_called_once()
        mock_instance.disconnect.assert_called_once()


@pytest.mark.asyncio
async def test_async_job_dispatcher_context_manager():
    mock_client = MagicMock(spec=NatsWorkClient)
    mock_client.connect = AsyncMock()
    mock_client.disconnect = AsyncMock()

    dispatcher = AsyncJobDispatcher(mock_client)

    async with dispatcher as d:
        assert d == dispatcher

    mock_client.connect.assert_called_once()
    mock_client.disconnect.assert_called_once()


@pytest.mark.asyncio
async def test_async_job_dispatcher_callable():
    mock_client = MagicMock(spec=NatsWorkClient)
    mock_client.perform_async = AsyncMock(return_value="job-123")

    dispatcher = AsyncJobDispatcher(mock_client)

    class TestJob:
        pass

    result = await dispatcher(TestJob, "arg1", kwarg="value")

    assert result == "job-123"
    mock_client.perform_async.assert_called_once_with(TestJob, "arg1", kwarg="value")
