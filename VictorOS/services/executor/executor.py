from VictorOS.contracts.execution_plan import ExecutionPlan
from VictorOS.services.brain.session import ChatSession


class Executor:

    def __init__(self, session: ChatSession):
        self.session = session

    def execute(self, plan: ExecutionPlan):

        return self.session.ask(
            plan.prompt,
            model=plan.model,
        )