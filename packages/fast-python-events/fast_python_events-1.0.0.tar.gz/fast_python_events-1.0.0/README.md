# Domain Events ⚡

Ultra-fast events system for Python, optimized for high performance and production-ready.

## Features

- 🚀 **7-8x faster** than Django Signals
- 💾 **Memory-efficient** 60% less usage compared to Django Signals
- 🔧 **Type-safe** with DTOs
- 🎯 **Simple and robust**
- 🔌 **Celery integration**

## Installation

### Core dependencies
```bash
pip install -r requirements/requirements.txt
```

### Cython acceleration (recommended for production)
Build and install the Cython module in editable mode so it's available throughout your environment:
```bash
pip install cython
pip install -e ./cython_core
```
This will compile and link the accelerated module automatically. No need to modify PYTHONPATH.

### Development dependencies
Includes everything needed for testing, benchmarks and development:
```bash
pip install -r requirements/requirements-dev.txt
```

## Quick Start

```python
from domain_events import DomainEventSystem, DomainEvent
from dataclasses import dataclass

@dataclass(frozen=True)
class UserRegisteredEvent(DomainEvent):
    event_type = "user.registered"
    user_id: int
    email: str

system = DomainEventSystem()

def send_welcome_email(event: UserRegisteredEvent):
    print(f"Welcome {event.email}!")

system.register_event(
    "user.registered",
    UserRegisteredEvent,
    [(send_welcome_email, {"async": True})]
)

event = UserRegisteredEvent(user_id=1, email="test@example.com")
system.publish(event)
```

## Python Integration

In your code:

```python
from domain_events import domain_events

domain_events.publish(user_event)
```

## Celery Integration

```python
from domain_events import DomainEventSystem
from celery import Celery

app = Celery()
event_system = DomainEventSystem(celery_app=app)
```

## Performance

- **Lookup:** 40-60ns (8x faster than Django Signals)
- **Dispatch (Cython):** 90-120ns per handler (typically 2-10x faster than pure Python)
- **Bulk dispatch (Cython):** up to 10x faster for large batches
- **Memory:** 60% less usage compared to Django Signals
- **Benchmark results:**
    - Cython event dispatch: ~110ns per handler (10 handlers, single event)
    - Python event dispatch: ~170ns per handler (10 handlers, single event)
    - Cython bulk dispatch: ~25μs for 1000 events
    - Python bulk dispatch: ~88μs for 1000 events

For best results in production, always enable Cython acceleration.
