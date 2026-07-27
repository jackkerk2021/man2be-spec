from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass(frozen=True)
class Event:
    id: UUID
    type: str

feat(events): add immutable Event base class
