import requests

from VictorOS.services.intent.builder import PromptPackage

from VictorOS.services.intent.prompts import UNDERSTANDING_SYSTEM_PROMPT


class IntentAdapter:

    def __init__(
        self,
        model="qwen3:0.6b",
        host="http://localhost:11434",
    ):
        self.model = model
        self.host = host.rstrip("/")

        self.session = requests.Session()

    def generate(self, package: PromptPackage) -> str:

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": package.system,
                },
                {
                    "role": "user",
                    "content": package.user,
                },
            ],
            "stream": False,
            "think": False,
            "options": {
                "temperature": 0,
            },
        }

        response = self.session.post(
            f"{self.host}/api/chat",
            json=payload,
            timeout=30,
        )

        response.raise_for_status()

        content = response.json()["message"]["content"]

        print("=" * 40)
        print("PLANNER RAW RESPONSE")
        print(content)
        print("=" * 40)

        return content.strip()

    def close(self):
        self.session.close()