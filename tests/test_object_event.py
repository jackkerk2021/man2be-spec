from src.events.object import ObjectEvent
from src.state.world_state import WorldState
from src.state.state_engine import StateEngine


def test_pickup_flashlight():

    state = WorldState()

    engine = StateEngine()

    event = ObjectEvent(
        actor="Jack",
        action="PickUp",
        target="Flashlight"
    )

    engine.apply(state, event)

    assert state.objects["Flashlight"]["owner"] == "Jack"
