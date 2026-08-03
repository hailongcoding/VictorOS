from VictorOS.core.contracts.execution_plan import ExecutionPlan
from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.understanding import Understanding


class ExecutionMapper:
    """
    Converts an Understanding into an ExecutionPlan.

    No AI.
    Pure deterministic mapping.
    """

    def map(
        self,
        understanding: Understanding,
    ) -> ExecutionPlan:

        requests: list[ExecutionRequest] = []

        for intent in understanding.intents:

            request = ExecutionRequest(

                capability="unknown",

                payload={

                    "goal": intent.goal,

                    "description": intent.description,

                    "entities": intent.entities,

                },

            )

            requests.append(request)

        return ExecutionPlan(

            goal=understanding.goal,

            requests=requests,

        )