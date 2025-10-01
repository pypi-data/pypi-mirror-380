import array
from threading import RLock
from typing import Callable, Dict, Tuple, Type

from .base import DomainEvent


class EventRegistry:
    def __init__(self):
        self._handler_funcs = array.array("Q")
        self._event_offsets = array.array("I", [0])
        self._async_flags = array.array("B")

        self._event_ids: Dict[str, int] = {}
        self._event_classes: Dict[str, Type[DomainEvent]] = {}
        self._next_id = 0
        self._lock = RLock()

    def register(self, event_type: str, event_class: Type[DomainEvent], handlers: list[Tuple[Callable, dict]]) -> None:
        with self._lock:
            if event_type not in self._event_ids:
                self._event_ids[event_type] = self._next_id
                self._event_classes[event_type] = event_class
                self._next_id += 1
                self._event_offsets.append(self._event_offsets[-1])

            event_id = self._event_ids[event_type]

            for handler_func, config in handlers:
                if not callable(handler_func):
                    raise ValueError(f"Handler {handler_func} no es callable")

                self._handler_funcs.append(id(handler_func))
                self._async_flags.append(1 if config.get("async", False) else 0)

            self._event_offsets[event_id + 1] += len(handlers)

    def get_handlers(self, event_id: int) -> Tuple[array.array, array.array]:
        start = self._event_offsets[event_id]
        end = self._event_offsets[event_id + 1]
        return self._handler_funcs[start:end], self._async_flags[start:end]

    def get_event_info(self, event_type: str) -> Dict:
        if event_type not in self._event_ids:
            return {}

        event_id = self._event_ids[event_type]
        start = self._event_offsets[event_id]
        end = self._event_offsets[event_id + 1]

        return {
            "event_id": event_id,
            "event_class": self._event_classes[event_type].__name__,
            "handlers_count": end - start,
        }
