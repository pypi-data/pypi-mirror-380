from contextlib import asynccontextmanager
from typing import List, Optional

from .client import NatsWorkClient


@asynccontextmanager
async def natswork_client(servers: Optional[List[str]] = None, **options):
    client = NatsWorkClient(servers=servers, **options)

    try:
        await client.connect()
        yield client
    finally:
        await client.disconnect()


class AsyncJobDispatcher:

    def __init__(self, client: NatsWorkClient):
        self.client = client

    async def __aenter__(self):
        await self.client.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.disconnect()

    async def __call__(self, job_class, *args, **kwargs):
        return await self.client.perform_async(job_class, *args, **kwargs)
