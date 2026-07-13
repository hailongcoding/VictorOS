from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import uuid


class TaskStatus(str, Enum):

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"

    CANCELLED = "cancelled"


@dataclass
class Task:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    prompt: str = ""

    status: TaskStatus = TaskStatus.PENDING

    result: str | None = None