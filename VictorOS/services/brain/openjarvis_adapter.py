from __future__ import annotations

from VictorOS.services.capabilities.manifest import ProviderManifest

from openjarvis import Jarvis

from VictorOS.services.brain.adapter import BrainAdapter

from VictorOS.core.contracts.execution_request import ExecutionRequest
from VictorOS.core.contracts.execution_result import ExecutionResult
from VictorOS.services.brain.session import ChatSession

import asyncio

import os


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


        prompt = ""

        for m in messages:

            role = m["role"]

            content = m["content"]

            prompt += f"{role.upper()}: {content}\n"


        import time

        start = time.perf_counter()

        result = self.jarvis.ask_full(
            prompt,
            agent="orchestrator",
            model=model
        )

        print(
            f"[Brain] {time.perf_counter()-start:.2f}s" 
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

    def execute(
        self,
        request: ExecutionRequest,
    ) -> ExecutionResult:

        session = ChatSession(self)

        prompt = (
            request.payload.get("prompt")
            or request.payload.get("goal")
            or ""
        )

        response = session.ask(prompt)

        return ExecutionResult(
            success=True,
            summary=response,
            artifacts=[],
            actions=[],
        )
    
    def get_manifest(self) -> ProviderManifest:
        return ProviderManifest(
            name="OpenJarvis",
            version="1.0",
            author="OpenJarvis",
            description="General intelligence provider",

            capabilities=[
                "conversation",
                "coding",
                "research",
            ],

            priority=10,
        )

    def close(self):
        self.jarvis.close()