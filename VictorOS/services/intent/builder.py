from dataclasses import dataclass

from VictorOS.services.intent.prompts import UNDERSTANDING_SYSTEM_PROMPT


@dataclass(slots=True)
class PromptPackage:
    system: str
    user: str


class UnderstandingPromptBuilder:

    def build(self, user_prompt: str) -> PromptPackage:

        return PromptPackage(
            system=UNDERSTANDING_SYSTEM_PROMPT,
            user=user_prompt.strip(),
        )