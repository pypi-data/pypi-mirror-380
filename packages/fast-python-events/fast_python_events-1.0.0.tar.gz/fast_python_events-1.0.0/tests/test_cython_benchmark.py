from dataclasses import dataclass

from cython_core.events_core import publish_event
from domain_events import DomainEvent


@dataclass(frozen=True)
class _BenchEvent(DomainEvent):
    data: str
    event_type = "bench.event"


def dummy_handler(event: _BenchEvent):
    pass


def test_cython_publish_event_benchmark(benchmark):
    handlers = [dummy_handler for _ in range(10)]
    event = _BenchEvent(data="payload")
    benchmark(publish_event, handlers, event)
    benchmark(publish_event, handlers, event)


def test_cython_bulk_publish_benchmark(benchmark):
    handlers = [dummy_handler]
    events = [_BenchEvent(data=str(i)) for i in range(1000)]

    def bulk_publish():
        for event in events:
            publish_event(handlers, event)

    benchmark(bulk_publish)
