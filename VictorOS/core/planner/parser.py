import re

from VictorOS.core.planner.raw_plan import RawPlan, RawTask
from VictorOS.core.contracts.task import Task

class PlannerParser:

    TASK_PATTERN = re.compile(
        r"GOAL:\s*(.*?)\s*CAPABILITIES:\s*(.*?)\s*END",
        re.DOTALL | re.IGNORECASE,
    )
    def parse(self, text: str) -> RawPlan:

        tasks = []

        for goal, caps in self.TASK_PATTERN.findall(text):

            print(f"[Parser] Goal: {goal}")
            print(f"[Parser] Capabilities: {caps}")

            capabilities = [
                c.strip().lower()
                for c in caps.split(",")
                if c.strip()
            ]

            tasks.append(
                RawTask(
                    goal=goal,
                    capabilities=capabilities,
                )
            )

        return RawPlan(tasks=tasks)