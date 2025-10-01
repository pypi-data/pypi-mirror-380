from domain_events.base import DomainEvent
from domain_events.config import EVENTS_CONFIG, register_project_events


class DummyEvent(DomainEvent):
    data: str
    event_type = "dummy.event"


registered = []


def dummy_handler(event):
    registered.append(event.data)


def test_register_project_events(monkeypatch):
    monkeypatch.setattr("domain_events.domain_events.register_event", lambda *a, **kw: registered.append("registered"))
    register_project_events(
        [{"event_type": "dummy.event", "event_class": DummyEvent, "handlers": [(dummy_handler, {})]}]
    )
    assert "registered" in registered
