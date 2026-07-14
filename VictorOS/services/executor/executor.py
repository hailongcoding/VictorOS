from VictorOS.contracts.execution_plan import ExecutionPlan
from VictorOS.services.brain.session import ChatSession
from VictorOS.services.brain.service import BrainService


class Executor:

    def __init__(self, brain: BrainService):
        self.brain = brain

    def execute(self, plan: ExecutionPlan):

        session = ChatSession(self.brain)

        return session.ask(
            plan.prompt,
            model=plan.model,
        )