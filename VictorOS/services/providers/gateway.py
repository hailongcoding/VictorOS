from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.execution_result import ExecutionResult

from VictorOS.services.capabilities.registry import CapabilityRegistry


class ProviderGateway:

    def __init__(
        self,
        registry: CapabilityRegistry,
    ):
        self.registry = registry

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:

        provider = self.registry.resolve(
            request.capability
        )

        if provider is None:
            raise RuntimeError(
                f"No provider registered for '{request.capability}'"
            )

        return provider.implementation.execute(
            request
        )