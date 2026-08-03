from VictorOS.core.contracts.execution_plan import ExecutionPlan
from VictorOS.core.contracts.task import Task

from VictorOS.core.planner.raw_plan import RawPlan


class PlannerValidator:

    ALIASES = {
        "general": "conversation",
        "general conversation": "conversation",
        "chat": "conversation",
    }

    def __init__(self, registry):
        self.registry = registry

    def validate(
        self,
        raw: RawPlan,
    ) -> ExecutionPlan:

        tasks = []

        valid_capabilities = {
            c.lower()
            for c in self.registry.capabilities()
        }

        counter = 1

        for raw_task in raw.tasks:

            capabilities = []

            for capability in raw_task.capabilities:

                capability = capability.strip().lower()

                capability = self.ALIASES.get(
                    capability,
                    capability,
                )

                if capability in valid_capabilities:
                    capabilities.append(capability)

            if not capabilities:
                continue

            tasks.append(
                Task(
                    id=f"task-{counter}",
                    goal=raw_task.goal,
                    capabilities=capabilities,
                )
            )

            counter += 1

        return ExecutionPlan(tasks=tasks)