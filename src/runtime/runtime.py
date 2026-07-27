state = WorldState()

engine = StateEngine()

event = ObjectEvent(

    actor="Jack",

    action="PickUp",

    target="Flashlight"

)

engine.apply(state, event)
