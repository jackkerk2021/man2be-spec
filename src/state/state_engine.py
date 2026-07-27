from events.object import ObjectEvent


class StateEngine:

    def apply(self, state, event):

        if isinstance(event, ObjectEvent):

            state.objects[event.target] = {
                "owner": event.actor
            }

feat(state): add StateEngine.apply()
