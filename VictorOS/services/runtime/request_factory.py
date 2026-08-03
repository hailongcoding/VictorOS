from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.reasoning import Decision

class ExecutionRequestFactory:

    def create(
        self,
        decision: Decision,
    ) -> ExecutionRequest:

        return ExecutionRequest(
            capability=decision.capability,
            payload={
                "goal": decision.goal,
                "reason": decision.reason,
            },
            metadata={
                "confidence": decision.confidence,
            },
        )