from django.apps import AppConfig


class DomainEventsConfig(AppConfig):
    name = "domain_events"
    verbose_name = "Domain Events System"

    def ready(self):
        from .config import setup_events

        setup_events()
