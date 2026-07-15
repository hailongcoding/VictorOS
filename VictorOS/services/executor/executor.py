from VictorOS.contracts.execution_plan import ExecutionPlan
from VictorOS.services.brain.session import ChatSession
from VictorOS.services.intelligence.gateway import IntelligenceGateway
from VictorOS.services.brain.session import ChatSession

from VictorOS.contracts.execution_result import ExecutionResult

class Executor:

    def __init__(self, gateway: IntelligenceGateway):
        self.gateway = gateway

    def execute(self, plan: ExecutionPlan):

        provider = self.gateway.provider(
            plan.task.value
        )

        session = ChatSession(provider)

        response = session.ask(
            plan.prompt,
            model=plan.model,
        )

        return ExecutionResult(
            success=True,
            summary=response,
            artifacts=[],
            actions=[],
        )