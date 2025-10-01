import asyncio
import threading
from temporalio import activity
from concurrent.futures import ThreadPoolExecutor
from .workflow_input import ActivityInput
from .auto_heart_beat import AutoHeartbeat


def create_activity_type(name: str):
    class ActivityBase:
        def __init__(self, is_heartbeat: bool = False, heartbeat_interval: int = 10):
            self.is_heartbeat = is_heartbeat
            self.heartbeat_interval = heartbeat_interval
            self._executor_pool = ThreadPoolExecutor(max_workers=1)

        @activity.defn(name=name)
        async def run(self, *args, **kwargs):
            if not self.is_heartbeat:
                return await self.executor(*args, **kwargs)
            else:
                return await self.heartbeat_runner(*args, **kwargs)

        async def heartbeat_runner(self, *args, **kwargs):
            async with AutoHeartbeat(interval=self.heartbeat_interval) as hb:
                event_cancel = asyncio.Event()

                def on_cancel():
                    event_cancel.set()
                hb.add_cancel_listener(on_cancel)
                try:
                    return await self._run_in_thread(self.executor, event_cancel, *args, **kwargs)
                except Exception as e:
                    raise e
                finally:
                    event_cancel.set()

        async def _run_in_thread(self, func, *args, **kwargs):
            loop = asyncio.get_event_loop()
            return await loop.run_in_executor(self._executor_pool, lambda: asyncio.run(func(*args, **kwargs)))

        async def executor(self, cancel_event: threading.Event, data: ActivityInput, *args, **kwargs):
            """ Override this method in subclasses to implement activity logic. """
            raise NotImplementedError("Executor must be implemented in subclass")
    return ActivityBase
