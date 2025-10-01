from dataclasses import dataclass

import pytest

from domain_events import DomainEvent, DomainEventSystem


@dataclass(frozen=True)
class _TestEvent(DomainEvent):
    data: str
    event_type = "test.event"


def test_basic_event_flow():
    system = DomainEventSystem()
    calls = []

    def handler(event: _TestEvent):
        calls.append(event.data)

    system.register_event("test.event", _TestEvent, [(handler, {})])

    event = _TestEvent(data="test")
    system.publish(event)

    assert calls == ["test"]
