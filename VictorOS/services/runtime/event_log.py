from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class EventRecord:
    timestamp: datetime
    event: str
    payload: dict[str, Any]


class EventLog:

    def __init__(self):
        self._records: list[EventRecord] = []

    def record(self, event: str, **payload):

        self._records.append(
            EventRecord(
                timestamp=datetime.now(),
                event=event,
                payload=payload,
            )
        )

    def all(self):
        return list(self._records)

    def clear(self):
        self._records.clear()