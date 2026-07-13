from __future__ import annotations

from collections import defaultdict
from typing import Any, Callable

EventCallback = Callable[[Any], None]


class EventBus:
    """Simple publish/subscribe event bus."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[EventCallback]] = defaultdict(list)

    def subscribe(self, event: str, callback: EventCallback) -> None:
        """Register a callback for an event."""

        if callback not in self._listeners[event]:
            self._listeners[event].append(callback)

    def unsubscribe(self, event: str, callback: EventCallback) -> None:
        """Remove a callback."""

        if callback in self._listeners[event]:
            self._listeners[event].remove(callback)

    def publish(self, event: str, data: Any = None) -> None:
        """Notify every listener."""

        for callback in self._listeners[event]:
            callback(data)