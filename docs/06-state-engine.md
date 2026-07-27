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

# Conflict Resolution

World State :

Jack

Location:

Cave

next line :

Jack suddenly appears at the airport.

State Engine：

Conflict

↓

Teleport?
Missing Transition

----

# Physical Rules

Mirror Gate

Closed

next chapter :

Jack walks through Mirror Gate.

State Engine：

Invalid World State

----


