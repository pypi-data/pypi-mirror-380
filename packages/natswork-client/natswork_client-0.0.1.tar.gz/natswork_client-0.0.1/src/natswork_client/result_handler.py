import asyncio
import logging
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional

from .exceptions import ClientTimeoutError
from .messages import MessageSerializer, ResultMessage
from .nats_client import NatsConnectionManager

logger = logging.getLogger(__name__)


@dataclass
class JobResult:
    job_id: str
    status: str
    result: Any = None
    error: Optional[str] = None
    completed_at: Optional[datetime] = None
    processing_time: Optional[float] = None


class ResultHandler:

    def __init__(self, connection_manager: NatsConnectionManager):
        self.connection_manager = connection_manager
        self._callbacks: Dict[str, List[Callable]] = defaultdict(list)
        self._result_futures: Dict[str, asyncio.Future] = {}
        self._subscription = None
        self._running = False

    async def start(self):
        if self._running:
            return

        self._running = True

        nc = await self.connection_manager.connect()

        self._subscription = await nc.subscribe("natswork.results.*", cb=self._handle_result_message)

        logger.info("Result handler started")

    async def stop(self):
        if not self._running:
            return

        self._running = False

        if self._subscription:
            await self._subscription.unsubscribe()
            self._subscription = None

        logger.info("Result handler stopped")

    def subscribe(self, callback: Callable[[JobResult], None], job_ids: List[str] = None):
        if job_ids:
            for job_id in job_ids:
                self._callbacks[job_id].append(callback)
        else:
            self._callbacks["*"].append(callback)

    async def wait_for_result(self, job_id: str, timeout: float = None) -> JobResult:
        if job_id in self._result_futures:
            future = self._result_futures[job_id]
        else:
            future = asyncio.Future()
            self._result_futures[job_id] = future

        try:
            if timeout:
                return await asyncio.wait_for(future, timeout=timeout)
            else:
                return await future
        except asyncio.TimeoutError:
            self._result_futures.pop(job_id, None)
            raise ClientTimeoutError(f"Timeout waiting for job {job_id} result")

    async def _handle_result_message(self, msg):
        try:
            result_message = MessageSerializer.deserialize(msg.data, ResultMessage)
            job_result = JobResult(
                job_id=result_message.job_id,
                status=result_message.status,
                result=result_message.result,
                error=result_message.error,
                completed_at=result_message.completed_at,
                processing_time=result_message.processing_time
            )

            if result_message.job_id in self._result_futures:
                future = self._result_futures.pop(result_message.job_id)
                if not future.done():
                    future.set_result(job_result)

            await self._call_callbacks(job_result)

        except Exception as e:
            logger.error(f"Error handling result message: {e}")

    async def _call_callbacks(self, job_result: JobResult):
        job_callbacks = self._callbacks.get(job_result.job_id, [])

        global_callbacks = self._callbacks.get("*", [])

        all_callbacks = job_callbacks + global_callbacks

        for callback in all_callbacks:
            try:
                if asyncio.iscoroutinefunction(callback):
                    await callback(job_result)
                else:
                    callback(job_result)
            except Exception as e:
                logger.error(f"Callback error for job {job_result.job_id}: {e}")
