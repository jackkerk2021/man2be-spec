# Reader

A Reader is responsible for interpreting a story source and extracting Events.

The Reader never generates media.

The Reader continuously updates the World State through Events.


# Principles

- Readers are source-independent.
- Readers never modify the story.
- Readers extract Events.
- Readers update the World State indirectly.
- Readers never generate Production YAML directly.

## Supported Sources

Novel

Screenplay

Comic

Subtitle

Game Script

Interactive Story

# Reader Flow

Story

↓

Read

↓

Interpret

↓

Extract Events

↓

Update World State

↓

Continue Reading


# Reader Responsibilities

The Reader is responsible for:

- Reading the story.
- Understanding story progression.
- Identifying meaningful Events.
- Maintaining reading order.
- Passing Events to the World State Engine.

  Example:

Story :  Jack picked up the flashlight.

Reader：

↓

Event：

Object Event:

Actor:
Jack

Action:
PickUp

Target:
Flashlight

↓

World State：

Flashlight

Owner:

Jack

Reader end here.


  


