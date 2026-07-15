from VictorOS.services.capabilities.registry import CapabilityRegistry


class IntelligenceGateway:

    def __init__(self, registry: CapabilityRegistry):
        self.registry = registry

    def provider(self, capability: str):

        provider = self.registry.resolve(capability)

        if provider is None:
            raise RuntimeError(
                f"No provider registered for '{capability}'."
            )

        return provider.implementation