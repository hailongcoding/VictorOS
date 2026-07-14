from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import itertools
from typing import Any


class TaskStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

_task_ids = itertools.count(1)
@dataclass
class Task:
    name: str
    payload: Any

    id: int = field(default_factory=lambda: next(_task_ids))

    status: TaskStatus = TaskStatus.QUEUED

    progress: int = 0

    current_step: str = "Waiting"

    result: str | None = None

    created_at: datetime = field(default_factory=datetime.now)

    started_at: datetime | None = None

    completed_at: datetime | None = None