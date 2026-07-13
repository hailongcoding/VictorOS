from dataclasses import dataclass
from enum import Enum
from typing import Any


class TaskStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    name: str
    payload: Any
    status: TaskStatus = TaskStatus.QUEUED
    result: str | None = None