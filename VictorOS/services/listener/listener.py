from openjarvis.core.events import get_event_bus, EventType


class JarvisListener:
    def __init__(self):
        self.bus = get_event_bus()
        self._started = False

    def start(self):
        if self._started:
            return

        self.bus.subscribe(
            EventType.INFERENCE_END,
            self.on_inference_end,
        )

        self.bus.subscribe(
            EventType.AGENT_TURN_END,
            self.on_agent_turn_end,
        )

        self._started = True

    def stop(self):
        if not self._started:
            return

        self.bus.unsubscribe(
            EventType.INFERENCE_END,
            self.on_inference_end,
        )

        self.bus.unsubscribe(
            EventType.AGENT_TURN_END,
            self.on_agent_turn_end,
        )

        self._started = False

    def on_inference_end(self, event):
        pass

    def on_agent_turn_end(self, event):
        pass