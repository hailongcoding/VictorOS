from dataclasses import dataclass

@dataclass
class Plugin:

    provider: object

    enabled: bool = True