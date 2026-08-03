from dataclasses import dataclass

from VictorOS.core.contracts.task import Task


@dataclass
class PlannerResult:

    tasks: list[Task]