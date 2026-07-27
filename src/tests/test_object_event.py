def test_pickup_flashlight():

  from events.object import ObjectEvent
from state.world_state import WorldState
from state.state_engine import StateEngine


def test_pickup_flashlight():

    state = WorldState()

    engine = StateEngine()

    event = ObjectEvent(

        id=None,

        type="ObjectEvent",

        actor="Jack",

        action="PickUp",

        target="Flashlight"

    )

    engine.apply(state, event)

    assert state.objects["Flashlight"]["owner"] == "Jack"

    assert ...
