from __future__ import annotations

from openjarvis import Jarvis

from VictorOS.services.brain.adapter import BrainAdapter

import asyncio

import os
print("Adapter file:", os.path.abspath(__file__))

class OpenJarvisAdapter(BrainAdapter):

    def __init__(
        self,
        model: str = "qwen3.5:4b",
    ):
        self.jarvis = Jarvis(model=model)


    def chat(
        self,
        messages: list[dict[str, str]],
        model=None
    ) -> str:
        import inspect

        print("Adapter source:", inspect.getsourcefile(self.__class__))

        prompt = ""

        for m in messages:

            role = m["role"]

            content = m["content"]

            prompt += f"{role.upper()}: {content}\n"

        print(f"[Brain] Using model: {model}")    

        result = self.jarvis.ask_full(
            prompt,
            agent="orchestrator",
            model=model
        )

        return result["content"]
    async def stream_chat(
        self,
        messages: list[dict[str, str]],
    ):
        prompt = ""

        for m in messages:
            prompt += f"{m['role'].upper()}: {m['content']}\n"

        async for token in self.jarvis.ask_stream(prompt):
            yield token

    def close(self):
        self.jarvis.close()