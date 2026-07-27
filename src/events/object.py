from dataclasses import dataclass
from .base import Event


@dataclass(frozen=True)
class ObjectEvent(Event):
    actor: str = ""
    action: str = ""
    target: str = ""

feat(events): add ObjectEvent
