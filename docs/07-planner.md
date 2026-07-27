# Planner

work progress :

Story

↓

Reader

↓

Events

↓

State Engine

↓

World State

↓

Planner

↓

Production YAML

↓

Builder

↓

Provider

---

# Planner

The Planner is responsible for deciding when and what media should be generated.

The Planner never modifies the World State.

The Planner consumes the current World State and produces Production YAML requests.

# Principles

The Planner is stateless.

The Planner never updates the World State.

The Planner uses the current World State.

The Planner decides production timing.

The Planner is provider-independent.

# Responsibilities

Receive World State

↓

Evaluate Story Progress

↓

Determine Production Timing

↓

Select Production Targets

↓

Generate Production Requests

----

# Example

World State :

Mirror Gate

State:
Opening

Jack:
Looking at the gate

Misaki:
Standing beside Jack

---

Planner decide :

Generate:

Wide Shot

Generate:

Close-up of Jack

Generate:

Close-up of Mirror Gate

----


