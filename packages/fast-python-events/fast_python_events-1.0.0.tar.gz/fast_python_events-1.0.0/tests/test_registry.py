import pytest

from domain_events.base import DomainEvent
from domain_events.registry import EventRegistry


class RegEvent(DomainEvent):
    data: str
    event_type = "reg.event"


def test_register_and_get_info():
    registry = EventRegistry()

    def handler(event):
        pass

    registry.register("reg.event", RegEvent, [(handler, {})])
    info = registry.get_event_info("reg.event")
    assert info["event_class"] == "RegEvent"
    assert info["handlers_count"] == 1


def test_get_handlers():
    registry = EventRegistry()

    def handler(event):
        pass

    registry.register("reg.event", RegEvent, [(handler, {})])
    event_id = registry._event_ids["reg.event"]
    handlers, flags = registry.get_handlers(event_id)
    assert len(handlers) == 1
    assert len(flags) == 1
