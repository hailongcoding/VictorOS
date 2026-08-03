from __future__ import annotations

from dataclasses import dataclass, field

from VictorOS.core.contracts.task import Task

@dataclass(slots=True)
class ExecutionPlan:

    tasks: list[Task]

    goal: str = ""

    metadata: dict = field(default_factory=dict)