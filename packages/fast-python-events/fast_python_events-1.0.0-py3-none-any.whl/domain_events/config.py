from . import domain_events

EVENTS_CONFIG = []


def setup_events():
    """Función para que los proyectos configuren sus eventos."""
    for config in EVENTS_CONFIG:
        domain_events.register_event(**config)


def register_project_events(events_config: list):
    """
    Permitir que proyectos externos registren sus eventos.

    Ejemplo:
        ```python
        from domain_events.config import register_project_events

        register_project_events(MY_PROJECT_EVENTS)
        ```
    """
    for config in events_config:
        domain_events.register_event(**config)
