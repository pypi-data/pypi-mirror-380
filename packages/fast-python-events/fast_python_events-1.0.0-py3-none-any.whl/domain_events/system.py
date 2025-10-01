from typing import Optional

from celery import Celery

from .base import DomainEvent
from .dispatcher import EventDispatcher
from .registry import EventRegistry


class DomainEventSystem:
    def __init__(self, celery_app: Optional[Celery] = None):
        self.registry = EventRegistry()
        self.dispatcher = EventDispatcher(self.registry, celery_app)

    def register_event(self, event_type: str, event_class: type, handlers: list) -> None:
        self.registry.register(event_type, event_class, handlers)
        self.dispatcher._build_handler_cache()

    def publish(self, event: DomainEvent) -> None:
        self.dispatcher.publish(event)

    def get_registry_info(self) -> dict:
        return {event_type: self.registry.get_event_info(event_type) for event_type in self.registry._event_ids}

    def flush(self) -> None:
        self.dispatcher.flush()
