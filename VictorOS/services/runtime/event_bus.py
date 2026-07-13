from collections import defaultdict
from typing import Callable

from .events import RuntimeEvent


class RuntimeEventBus:

    def __init__(self):
        self._listeners = defaultdict(list)

    def subscribe(self, event: RuntimeEvent, callback: Callable):

        self._listeners[event].append(callback)

    def publish(self, event: RuntimeEvent, **payload):

        for callback in self._listeners[event]:
            callback(**payload)