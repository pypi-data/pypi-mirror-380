"""Unit tests for NatsWorkClient."""

from natswork_client.client import (
    ConfigurableClient,
    NatsWorkClient,
    get_default_client,
)
from natswork_client.config import ClientConfig


class TestNatsWorkClient:
    """Test cases for NatsWorkClient."""

    def test_init(self):
        """Test client initialization."""
        client = NatsWorkClient()
        assert client.servers == ["nats://localhost:4222"]
        assert client._connected is False

        client = NatsWorkClient(servers=["nats://example.com:4222"])
        assert client.servers == ["nats://example.com:4222"]

    def test_get_default_client(self):
        """Test get_default_client returns singleton."""
        client1 = get_default_client()
        client2 = get_default_client()
        assert client1 is client2

    def test_configurable_client(self):
        """Test ConfigurableClient with custom config."""
        config = ClientConfig(servers=["nats://test:4222"])
        client = ConfigurableClient(config)
        assert client.servers == ["nats://test:4222"]
        assert client.config == config
