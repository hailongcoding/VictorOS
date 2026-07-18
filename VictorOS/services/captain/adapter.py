import json

from VictorOS.contracts.captain_response import CaptainResponse

import requests

from VictorOS.services.brain.adapter import BrainAdapter
from VictorOS.services.capabilities.manifest import ProviderManifest

from .prompts import CAPTAIN_SYSTEM_PROMPT


class CaptainAdapter(BrainAdapter):
    import json

    from VictorOS.contracts.captain_response import CaptainResponse

    def handle(self, prompt: str):

        raw = self.chat(
            [
                {
                    "role": "user",
                    "content": prompt,
                }
            ]
        )

        text = raw.strip()

        upper = text.upper()

        if upper.startswith("ACTION: DELEGATE"):

            speak = text.split("\n", 1)[1].strip()

            return CaptainResponse(
                action="delegate",
                reply=speak,
                use_brain=True,
            )

        if upper.startswith("ACTION: ANSWER"):

            speak = text.split("\n", 1)[1].strip()

            return CaptainResponse(
                action="reply",
                reply=speak,
                use_brain=False,
            )

        return CaptainResponse(
            action="reply",
            reply=text,
            use_brain=False,
        )

    def __init__(
        self,
        model="qwen3:0.6b",
        host="http://localhost:11434",
    ):
        self.model = model
        self.host = host.rstrip("/")

        self.session = requests.Session()

        self.headers = {
            "Content-Type": "application/json",
        }

    def chat(
        self,
        messages,
        model=None,
    ):
        payload = {
            "model": model or self.model,
            "messages": [
                {
                    "role": "system",
                    "content": CAPTAIN_SYSTEM_PROMPT,
                },
                *messages,
            ],
            "stream": False,
            "think": False,
        }

        print("=" * 40)
        print("CAPTAIN MODEL")
        print(payload["model"])
        print("=" * 40)


        response = self.session.post(
            f"{self.host}/api/chat",
            json=payload,
            headers=self.headers,
            timeout=60,
        )


        response.raise_for_status()

        content = response.json()["message"]["content"]

        return content
    
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
        self.session.close()