import json

import requests


from VictorOS.services.ai.provider import AIProvider

class OllamaProvider(AIProvider):
    def __init__(
        self,
        host: str = "http://localhost:11434",
    ):
        self.host = host.rstrip("/")

        self.session = requests.Session()

        self.headers = {
            "Content-Type": "application/json"
        }

    def chat(
        self,
        *,
        model: str,
        messages: list[dict],
        stream: bool = False,
        think: bool = False,
    ) -> str:
        
        

        payload = {
            "model": model,
            "messages": messages,
            "stream": stream,
            "think": think,
        }

        try:
            import time

            start = time.perf_counter()

            response = self.session.post(
                f"{self.host}/api/chat",
                json=payload,
                headers=self.headers,
                timeout=180,
                stream=True,
            )

            elapsed = time.perf_counter() - start



            response.raise_for_status()

            full_response = ""

            for line in response.iter_lines():

                if not line:
                    continue

                chunk = json.loads(line)

                if "message" not in chunk:
                    continue

                token = chunk["message"].get("content", "")

                if token:
                    full_response += token

            return full_response.strip()
        except requests.exceptions.ReadTimeout:

            return (
                "Sorry sir, I took too long to respond.\n"
                "The model is probably still generating."
            )

        except requests.exceptions.ConnectionError:

            return (
                "I can't reach the Ollama server.\n"
                "Is Ollama running?"
            )

        except requests.exceptions.RequestException as e:

            return "An unexpected network error occurred."