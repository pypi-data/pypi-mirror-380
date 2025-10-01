import logging

from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def process_async_batch(batch: list) -> None:
    for handlers, event in batch:
        for handler in handlers:
            try:
                handler(event)
            except Exception as e:
                logger.error(f"Async handler failed: {e}")
