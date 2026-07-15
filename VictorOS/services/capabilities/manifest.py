from dataclasses import dataclass

@dataclass
class ProviderManifest:
    name: str
    version: str
    author: str
    description: str

    capabilities: list[str]

    priority: int = 100