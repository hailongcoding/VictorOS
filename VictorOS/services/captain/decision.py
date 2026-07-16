from dataclasses import dataclass


@dataclass
class CaptainDecision:
    handled: bool
    response: str | None = None