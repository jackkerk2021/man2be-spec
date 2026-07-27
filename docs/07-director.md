# Director

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

Director

↓

Production YAML

↓

Builder

↓

Provider

---

# Director

The Director is responsible for deciding when and what media should be generated.

The Director never modifies the World State.

The Director consumes the current World State and produces Production YAML requests.

# Principles

The Director is stateless.

The Director never updates the World State.

The Director uses the current World State.

The Director decides production timing.

The Director is provider-independent.

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

Director decide :

Generate:

Wide Shot

Generate:

Close-up of Jack

Generate:

Close-up of Mirror Gate

----


