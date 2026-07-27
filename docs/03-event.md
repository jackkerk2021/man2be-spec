# Event

An Event represents a meaningful change in the story.

Events are extracted from the story by the Reader.

Every World State update must originate from one or more Events.

- Events are immutable.
- Events occur in chronological order.
- Events update the World State.
- Events never generate media directly.
- Multiple Events may exist in a single sentence.

## Event Types

Character Event

Object Event

Location Event

Environment Event

Dialogue Event

Relationship Event

Emotion Event

Timeline Event

System Event

## Event Types

Character Event

Object Event

Location Event

Environment Event

Dialogue Event

Relationship Event

Emotion Event

Timeline Event

System Event

## Event Flow

Novel

↓

Reader

↓

Event Extractor

↓

Events

↓

World State Engine

↓

Updated World State

## Example

Jack picked up the flashlight.


EVT-00027

type:
ObjectEvent

actor:
Jack

action:
PickUp

target:
Flashlight

## Event Life Cycle

Story

↓

Reader

↓

Event

↓

World State Update

↓

Production YAML

↓

Media Generation
