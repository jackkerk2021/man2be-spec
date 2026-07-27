from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Event:
    id: UUID = field(default_factory=uuid4)
    type: str = ""

feat(events): add immutable Event base class
