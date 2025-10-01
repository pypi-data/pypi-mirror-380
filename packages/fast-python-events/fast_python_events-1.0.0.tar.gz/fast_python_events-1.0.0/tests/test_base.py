from dataclasses import dataclass

import pytest

from domain_events.base import DomainEvent


@dataclass(frozen=True)
class _MyEvent(DomainEvent):
    data: str
    event_type = "my.event"


def test_event_type_required():
    class NoTypeEvent(DomainEvent):
        pass

    with pytest.raises(ValueError):
        NoTypeEvent()


def test_event_fields():
    event = _MyEvent(data="info")
    assert event.event_type == "my.event"
    assert event.data == "info"
    assert event.version == 1
    assert event.event_id
    assert event.occurred_on
