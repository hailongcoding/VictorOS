from VictorOS.services.ai.client import AIClient

from VictorOS.services.intent.builder import PromptPackage
from VictorOS.core.planner.prompts import PLANNER_SYSTEM_PROMPT


class PlannerAdapter:

    def __init__(self, client: AIClient):

        self.client = client

    def generate(
        self,
        prompt: str,
        capabilities: list[str],
    ):
        package = PromptPackage(
            system=PLANNER_SYSTEM_PROMPT.format(
                capability_list="\n".join(
                    f"- {c}"
                    for c in capabilities
                )
            ),
            user=prompt,
        )

        return self.client.chat(
            model="qwen3:0.6b",
            package=package,
            think=False,
        )