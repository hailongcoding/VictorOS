from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETE = "complete"
    FAILED = "failed"


@dataclass
class Task:

    id: str

    goal: str

    capabilities: list[str]

    status: TaskStatus = TaskStatus.PENDING

    result: Any | None = None

    metadata: dict = field(default_factory=dict)