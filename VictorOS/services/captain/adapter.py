from openjarvis import Jarvis

from VictorOS.services.brain.adapter import BrainAdapter
from VictorOS.services.capabilities.manifest import ProviderManifest

from .prompts import CAPTAIN_SYSTEM_PROMPT


class CaptainAdapter(BrainAdapter):

    def __init__(self):
        self.jarvis = Jarvis(
            model="qwen3:0.6b"
        )

    def chat(
        self,
        messages,
        model=None,
    ):
        prompt = CAPTAIN_SYSTEM_PROMPT + "\n\n"

        for message in messages:
            prompt += (
                f"{message['role'].upper()}: "
                f"{message['content']}\n"
            )

        result = self.jarvis.ask_full(
            prompt,
            agent="orchestrator",
            model=model,
        )

        return result["content"]

    async def stream_chat(self, messages):

        prompt = CAPTAIN_SYSTEM_PROMPT + "\n\n"

        for message in messages:
            prompt += (
                f"{message['role'].upper()}: "
                f"{message['content']}\n"
            )

        async for token in self.jarvis.ask_stream(prompt):
            yield token

    def get_manifest(self):
        return ProviderManifest(
            name="Captain",
            version="1.0",
            author="VictorOS",
            description="Executive AI",

            capabilities=[
                "captain",
            ],

            priority=100,
        )

    def close(self):
        self.jarvis.close()