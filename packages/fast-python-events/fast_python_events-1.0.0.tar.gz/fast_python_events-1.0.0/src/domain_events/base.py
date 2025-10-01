import uuid
from abc import ABC
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar


@dataclass(frozen=True, kw_only=True)
class DomainEvent(ABC):
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    occurred_on: datetime = field(default_factory=datetime.now)
    event_type: ClassVar[str]
    version: int = 1

    def __post_init__(self):
        if not hasattr(self, "event_type") or not self.event_type:
            raise ValueError("Subclasses must define event_type")
