from VictorOS.services.providers.gateway import ProviderGateway

from VictorOS.core.contracts.execution_result import ExecutionResult
from VictorOS.core.contracts.execution_request import ExecutionRequest


class Executor:

    def __init__(self, gateway: ProviderGateway):
        self.gateway = gateway

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:

        return self.gateway.execute(request)