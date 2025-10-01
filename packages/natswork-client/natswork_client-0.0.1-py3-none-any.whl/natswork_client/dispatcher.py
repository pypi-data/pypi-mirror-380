import asyncio
import logging
import time
from dataclasses import dataclass
from typing import Any, Dict, Tuple, Type

from .exceptions import ClientError, ClientTimeoutError, JobExecutionError
from .job import Job, JobRegistry
from .messages import MessageBuilder, MessageSerializer
from .nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


@dataclass
class PendingRequest:
    job_id: str
    future: asyncio.Future
    timeout_at: float


class JobDispatcher:

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager
        self._pending_requests: Dict[str, PendingRequest] = {}
        self._timeout_task = None

    async def start(self):
        if self._timeout_task is None:
            self._timeout_task = asyncio.create_task(self._handle_request_timeouts())

    async def stop(self):
        if self._timeout_task:
            self._timeout_task.cancel()
            try:
                await self._timeout_task
            except asyncio.CancelledError:
                pass
            self._timeout_task = None

    async def dispatch_async(self, job_class: Type[Job], args: Tuple, kwargs: Dict) -> str:
        job_name = f"{job_class.__module__}.{job_class.__name__}"
        job_config = JobRegistry.get_job_config(job_name)

        if not job_config:
            raise ClientError(f"Job class {job_name} not registered")

        arguments = list(args)
        if kwargs:
            arguments = {"args": list(args), **kwargs}

        job_message = MessageBuilder.build_job_message(
            job_class=job_name,
            queue=job_config.queue,
            arguments=arguments
        )

        nc = await self.connection_manager.connect()
        js = nc.jetstream()

        subject = f"natswork.jobs.{job_config.queue}"
        data = MessageSerializer.serialize(job_message)

        await js.publish(subject, data)

        logger.info(f"Dispatched async job {job_message.job_id} to queue {job_config.queue}")
        return job_message.job_id

    async def dispatch_sync(self, job_class: Type[Job], args: Tuple, kwargs: Dict, timeout: float) -> Any:
        from .messages import ResultMessage

        job_name = f"{job_class.__module__}.{job_class.__name__}"
        job_config = JobRegistry.get_job_config(job_name)

        if not job_config:
            raise ClientError(f"Job class {job_name} not registered")

        arguments = list(args)
        if kwargs:
            arguments = {"args": list(args), **kwargs}

        job_message = MessageBuilder.build_job_message(
            job_class=job_name,
            queue=job_config.queue,
            arguments=arguments
        )

        try:
            nc = await self.connection_manager.connect()
            subject = f"natswork.sync.{job_config.queue}"
            data = MessageSerializer.serialize(job_message)

            reply_data = await nc.request(subject, data, timeout=timeout)
            result_message = MessageSerializer.deserialize(reply_data.data, ResultMessage)

            if result_message.status == "success":
                return result_message.result
            elif result_message.status == "error":
                raise JobExecutionError(f"Job failed: {result_message.error}")
            else:
                raise ClientError(f"Unexpected job status: {result_message.status}")

        except asyncio.TimeoutError:
            raise ClientTimeoutError(f"Job {job_message.job_id} timed out after {timeout}s")

    async def _handle_request_timeouts(self):
        while True:
            try:
                current_time = time.time()
                expired_requests = [
                    req for req in self._pending_requests.values()
                    if req.timeout_at <= current_time
                ]

                for request in expired_requests:
                    if not request.future.done():
                        request.future.set_exception(
                            ClientTimeoutError(f"Request {request.job_id} timed out")
                        )
                    self._pending_requests.pop(request.job_id, None)

                await asyncio.sleep(1)

            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error in timeout handler: {e}")
                await asyncio.sleep(1)
