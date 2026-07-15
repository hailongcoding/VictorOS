from dataclasses import dataclass
from .provider_status import ProviderStatus



@dataclass
class CapabilityProvider:
    name: str
    capability: str
    implementation: object
    priority: int = 100
    status: ProviderStatus = ProviderStatus.ONLINE