from dataclasses import dataclass

from .intents import CaptainIntent


@dataclass
class CaptainDecision:

    intent: CaptainIntent

    speak: str

    use_brain: bool

    original_prompt: str = ""