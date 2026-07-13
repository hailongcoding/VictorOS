from __future__ import annotations

from abc import ABC, abstractmethod

import requests


class BrainAdapter(ABC):
    @abstractmethod
    def chat(self, messages: list[dict[str, str]]) -> str:
        ...

class DummyAdapter(BrainAdapter):

    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:

        last = messages[-1]["content"]

        return f"I heard: {last}"


class OllamaAdapter(BrainAdapter):
    def __init__(
        self,
        model: str = "qwen3.5:4b",
        host: str = "http://localhost:11434",
    ):
        self.model = model
        self.host = host.rstrip("/")

        # Persistent HTTP session
        self.session = requests.Session()   

        self.headers = {
            "Content-Type": "application/json"
        }    

    def chat(
        self,
        messages: list[dict[str, str]],
    ) -> str:
        
        import json

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": True,
            "think": False,
        }

        try:
            import time

            start = time.perf_counter()

            print("Sending request...")
            response = self.session.post(
                f"{self.host}/api/chat",
                json=payload,
                headers=self.headers,
                timeout=180,
                stream=True,
            )

            elapsed = time.perf_counter() - start

            print(f"Response received in {elapsed:.2f} seconds")
            print("=" * 40)


            response.raise_for_status()

            import json

            full_response = ""

            for line in response.iter_lines():

                if not line:
                    continue

                chunk = json.loads(line)

                if "message" in chunk:

                    token = chunk["message"].get("content", "")

                    if token:

                        print(token, end="", flush=True)

                        full_response += token

            print()

            return full_response.strip()
        except requests.exceptions.ReadTimeout:

            print("\n=== REQUEST TIMED OUT ===")
            return (
                "Sorry sir, I took too long to respond.\n"
                "The model is probably still generating."
            )

        except requests.exceptions.ConnectionError:

            print("\n=== CONNECTION ERROR ===")
            return (
                "I can't reach the Ollama server.\n"
                "Is Ollama running?"
            )

        except requests.exceptions.RequestException as e:

            print(f"\n=== REQUEST FAILED ===\n{e}")
            return "An unexpected network error occurred."