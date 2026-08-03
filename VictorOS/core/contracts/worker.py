from abc import ABC, abstractmethod

from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.execution_result import ExecutionResult


class Worker(ABC):

    @abstractmethod
    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:
        pass