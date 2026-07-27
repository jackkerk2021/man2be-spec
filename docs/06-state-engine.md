# State Engine

# Definition

The State Engine is responsible for applying Events to the World State.

It is the only component allowed to modify the World State.

---

Events are read-only.

World State is mutable.

Only the State Engine may update the World State.

Every update must originate from Events.

Updates must preserve story continuity.

---

# Responsibilities

Receive Events

↓

Validate Events

↓

Apply State Changes

↓

Resolve Conflicts

↓

Update World State

---

