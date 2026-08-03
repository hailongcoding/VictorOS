from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.execution_result import ExecutionResult
from VictorOS.services.executor.executor import Executor
from VictorOS.core.contracts.worker import Worker


class DefaultWorker(Worker):

    def __init__(self, executor: Executor):
        self.executor = executor

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:
        return self.executor.execute(request)