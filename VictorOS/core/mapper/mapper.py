from VictorOS.core.contracts.execution_plan import ExecutionPlan
from VictorOS.core.contracts.task import Task


class ExecutionMapper:

    def map(self, understanding) -> ExecutionPlan:

        capability = self._capability_for(understanding)

        task = Task(
            id="",
            goal=understanding.original_prompt,
            capabilities=[capability],
        )

        return ExecutionPlan(
            goal=understanding.original_prompt,
            tasks=[task],
        )

    def _capability_for(self, understanding):

        intent = understanding.intent.name.lower()

        mapping = {

            "conversation": "conversation",

            "chat": "conversation",

            "greeting": "conversation",

            "coding": "coding",

            "code_generation": "coding",

            "research": "research",

            "search": "research",

            "browser": "browser",

        }

        return mapping.get(intent, "conversation")