"""Integration tests for NatsWorkClient."""

import pytest


@pytest.mark.integration
class TestNatsWorkClientIntegration:
    """Integration test cases for NatsWorkClient."""

    @pytest.mark.asyncio
    async def test_client_connection(self, nats_url):
        """Test client can connect to NATS server."""
        from natswork_client.nats_client import NatsConnectionManager

        manager = NatsConnectionManager(servers=[nats_url])
        nc = await manager.connect()

        assert nc is not None
        assert manager._connected is True

        await manager.disconnect()
        assert manager._connected is False

    @pytest.mark.asyncio
    async def test_job_dispatch_async(self, nats_url):
        """Test async job dispatch."""
        from natswork_client.messages import MessageBuilder, MessageSerializer
        from natswork_client.nats_client import (
            JetStreamClient,
            NatsConnectionManager,
            StreamManager,
        )

        manager = NatsConnectionManager(servers=[nats_url])
        await manager.connect()

        js_client = JetStreamClient(manager)
        stream_manager = StreamManager(js_client)

        # Ensure stream exists for test queue
        await stream_manager.ensure_job_stream("test")

        # Build and publish a job message
        job_msg = MessageBuilder.build_job_message(
            job_class="TestJob",
            queue="test",
            arguments={"arg1": "value1"}
        )

        data = MessageSerializer.serialize(job_msg)
        seq = await js_client.publish_async("natswork.jobs.test", data)

        assert seq > 0

        await manager.disconnect()

    @pytest.mark.asyncio
    async def test_job_dispatch_sync(self, nats_url):
        """Test sync job dispatch with request-reply pattern."""
        import asyncio

        from natswork_client.messages import (
            MessageBuilder,
            MessageSerializer,
            ResultMessage,
        )
        from natswork_client.nats_client import CoreNatsClient, NatsConnectionManager

        manager = NatsConnectionManager(servers=[nats_url])
        await manager.connect()

        core_client = CoreNatsClient(manager)

        # Set up a mock responder first
        async def mock_responder(msg):
            # Deserialize request
            from natswork_client.messages import JobMessage
            request = MessageSerializer.deserialize(msg.data, JobMessage)

            # Create and send response
            result_msg = MessageBuilder.build_result_message(
                job_id=request.job_id,
                status="success",
                result={"output": "test_result"},
                processing_time=0.1
            )
            response_data = MessageSerializer.serialize(result_msg)
            await manager._connection.publish(msg.reply, response_data)

        # Subscribe responder
        await core_client.subscribe("natswork.sync.test", mock_responder, queue="test_workers")
        await asyncio.sleep(0.5)  # Give subscription time to register

        # Send request
        job_msg = MessageBuilder.build_job_message(
            job_class="TestJob",
            queue="test",
            arguments={"arg1": "value1"}
        )
        request_data = MessageSerializer.serialize(job_msg)

        response_data = await core_client.request("natswork.sync.test", request_data, timeout=2.0)
        result_msg = MessageSerializer.deserialize(response_data, ResultMessage)

        assert result_msg.status == "success"
        assert result_msg.result == {"output": "test_result"}

        await manager.disconnect()
