from dataclasses import dataclass

from domain_events import DomainEvent, DomainEventSystem


@dataclass(frozen=True)
class _BenchEvent(DomainEvent):
    data: str
    event_type = "bench.event"


def dummy_handler(event: _BenchEvent):
    pass


def test_publish_event_benchmark(benchmark):
    system = DomainEventSystem()
    system.register_event("bench.event", _BenchEvent, [(dummy_handler, {})])
    event = _BenchEvent(data="payload")
    benchmark(system.publish, event)


def test_bulk_publish_benchmark(benchmark):
    system = DomainEventSystem()
    system.register_event("bench.event", _BenchEvent, [(dummy_handler, {})])
    events = [_BenchEvent(data=str(i)) for i in range(1000)]

    def bulk_publish():
        for event in events:
            system.publish(event)

    benchmark(bulk_publish)
