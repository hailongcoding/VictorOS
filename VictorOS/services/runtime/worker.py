from abc import ABC, abstractmethod

from VictorOS.contracts.execution_plan import ExecutionPlan


class Worker(ABC):

    @abstractmethod
    def execute(self, plan: ExecutionPlan):
        pass