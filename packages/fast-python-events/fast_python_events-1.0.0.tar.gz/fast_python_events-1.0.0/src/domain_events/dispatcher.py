import ctypes
from collections import deque
from threading import Lock
from typing import Callable, Dict, List, Tuple

from celery import Celery

from cython_core.events_core import publish_batch, publish_event

from .base import DomainEvent
from .tasks import process_async_batch

ASYNC_BUFFER_SIZE = 1000
MAX_SYNC_ERRORS = 5


class EventDispatcher:
    def __init__(self, registry: "EventRegistry", celery_app: Celery = None):
        self.registry = registry
        self.celery_app = celery_app

        try:
            from cython_bench.events_core import (
                publish_batch,
                publish_event,
                publish_event_metrics,
            )

            CYTHON_AVAILABLE = True
        except ImportError:
            CYTHON_AVAILABLE = False

        self._async_buffer = deque(maxlen=ASYNC_BUFFER_SIZE)
        self._async_lock = Lock()

        self._handler_cache: Dict[int, Tuple[List[Callable], List[Callable]]] = {}
        self._build_handler_cache()

    def _build_handler_cache(self) -> None:
        for event_type, event_id in self.registry._event_ids.items():
            handler_ptrs, async_flags = self.registry.get_handlers(event_id)

            sync_handlers = []
            async_handlers = []

            for i in range(len(handler_ptrs)):
                handler = ctypes.cast(handler_ptrs[i], ctypes.py_object).value
                if async_flags[i]:
                    async_handlers.append(handler)
                else:
                    sync_handlers.append(handler)

            self._handler_cache[event_id] = (sync_handlers, async_handlers)

    def publish(self, event: DomainEvent) -> None:
        event_type = event.event_type

        if event_type not in self.registry._event_ids:
            return

        event_id = self.registry._event_ids[event_type]
        sync_handlers, async_handlers = self._handler_cache[event_id]

        publish_event(sync_handlers, event)

        if async_handlers:
            self._enqueue_async_batch(async_handlers, event)

    def _enqueue_async_batch(self, handlers: List[Callable], event: DomainEvent) -> None:
        with self._async_lock:
            self._async_buffer.append((handlers, event))

            if len(self._async_buffer) >= ASYNC_BUFFER_SIZE:
                self._flush_async_buffer()

    def _flush_async_buffer(self) -> None:
        if not self._async_buffer:
            return

        batch = list(self._async_buffer)
        self._async_buffer.clear()

        if self.celery_app:
            process_async_batch.delay(batch)
        else:
            self._process_batch_sync(batch)

    def _process_batch_sync(self, batch: List[Tuple]) -> None:
        for handlers, event in batch:
            for handlers, event in batch:
                publish_event(handlers, event)

    def flush(self) -> None:
        self._flush_async_buffer()
