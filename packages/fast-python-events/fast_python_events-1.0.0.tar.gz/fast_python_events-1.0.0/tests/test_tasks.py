from domain_events.tasks import process_async_batch


class DummyEvent:
    pass


def test_process_async_batch_handles():
    called = []

    def handler(event):
        called.append(True)

    batch = [([handler], DummyEvent())]
    process_async_batch(batch)
    assert called == [True]
