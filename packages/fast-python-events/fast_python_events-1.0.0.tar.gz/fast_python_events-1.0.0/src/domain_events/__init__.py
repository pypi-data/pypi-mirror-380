"""
Domain Events - Sistema ultra-rápido de eventos de dominio para Python.
"""

__version__ = "1.0.0"

from .base import DomainEvent
from .dispatcher import EventDispatcher
from .registry import EventRegistry
from .system import DomainEventSystem

# Instancia global para uso rápido
domain_events = DomainEventSystem()

__all__ = [
    "DomainEvent",
    "EventRegistry",
    "EventDispatcher",
    "DomainEventSystem",
    "domain_events",
]
