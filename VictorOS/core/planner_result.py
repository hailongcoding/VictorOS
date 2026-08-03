from dataclasses import dataclass, field

@dataclass
class PlannerResult:

    tasks: list[Task]