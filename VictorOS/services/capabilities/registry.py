from collections import defaultdict

from .provider import CapabilityProvider

from .provider_status import ProviderStatus


class CapabilityRegistry:

    def __init__(self):
        self._providers = defaultdict(list)

    def register(self, provider: CapabilityProvider):

        self._providers[
            provider.capability
        ].append(provider)

        self._providers[
            provider.capability
        ].sort(
            key=lambda p: p.priority
        )

    def providers(self, capability: str):

        return list(
            self._providers.get(
                capability,
                []
            )
        )

    def resolve(self, capability: str):

        providers = self.providers(capability)

        if not providers:
            return None

        return providers[0]

    def capabilities(self):

        return sorted(
            self._providers.keys()
        )

    def online(self):

        return [
            provider
            for providers in self._providers.values()
            for provider in providers
            if provider.status == ProviderStatus.ONLINE
        ]
        
    def provider(self, name):

        for providers in self._providers.values():

            for provider in providers:

                if provider.name == name:

                    return provider

        return None
        
    def disable(self, name):

        provider = self.provider(name)

        if provider:

            provider.status = ProviderStatus.DISABLED

    def enable(self, name):

        provider = self.provider(name)

        if provider:

            provider.status = ProviderStatus.ONLINE