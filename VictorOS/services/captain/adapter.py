import requests

from VictorOS.services.brain.adapter import BrainAdapter
from VictorOS.services.capabilities.manifest import ProviderManifest

from .prompts import CAPTAIN_SYSTEM_PROMPT


class CaptainAdapter(BrainAdapter):

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

        import time

        start = time.perf_counter()

        response = self.session.post(
            f"{self.host}/api/chat",
            json=payload,
            headers=self.headers,
            timeout=60,
        )

        elapsed = time.perf_counter() - start

        print(f"[Captain] HTTP: {elapsed:.2f}s")

        response.raise_for_status()

        content = response.json()["message"]["content"]

        total = time.perf_counter() - start

        print(f"[Captain] Total: {total:.2f}s")

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