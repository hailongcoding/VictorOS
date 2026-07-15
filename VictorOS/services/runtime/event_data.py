from dataclasses import dataclass

from VictorOS.services.task_manager.task import Task


@dataclass
class RuntimeEventData:

    task: Task

    response: str | None = None

    error: Exception | None = None