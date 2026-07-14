from collections import defaultdict
from typing import Callable

from .events import RuntimeEvent

from .event_log import EventLog


class RuntimeEventBus:

    def __init__(self):
        self._listeners = defaultdict(list)
        self._log = EventLog()

    def subscribe(self, event: RuntimeEvent, callback: Callable):

        self._listeners[event].append(callback)

    def publish(self, event: RuntimeEvent, **payload):

        self._log.record(
            event.value,
            **payload,
        )

        for callback in self._listeners[event]:
            callback(**payload)
        
    def history(self):
        return self._log.all()