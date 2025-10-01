from dataclasses import dataclass

import pytest

from domain_events.base import DomainEvent
from domain_events.dispatcher import EventDispatcher
from domain_events.registry import EventRegistry


@dataclass(frozen=True)
class _TestEvent(DomainEvent):
    data: str
    event_type = "test.dispatch"


def test_sync_handler_execution():
    registry = EventRegistry()
    calls = []

    def handler(event):
        calls.append(event.data)

    registry.register("test.dispatch", _TestEvent, [(handler, {})])
    dispatcher = EventDispatcher(registry)
    dispatcher.publish(_TestEvent(data="ok"))
    assert calls == ["ok"]


def test_no_event_type():
    registry = EventRegistry()
    dispatcher = EventDispatcher(registry)

    class Dummy(DomainEvent):
        event_type = "not.registered"

    dispatcher.publish(Dummy())  # Should not fail
