from __future__ import annotations

from VictorOS.services.brain.service import BrainService


class ChatSession:
    """Represents one conversation with the AI."""

    def __init__(self, brain: BrainService) -> None:
        self.brain = brain
        self.history: list[dict[str, str]] = []
        

    def ask(self, prompt: str,model=None) -> str:
        print(f"[Session] model = {model}")
        self.history.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        print("\n===== HISTORY =====")

        for i, msg in enumerate(self.history):
            print(f"{i}: {msg['role']}")
            print(msg["content"])
            print("-" * 40)

        response = self.brain.chat(self.history,model=model)

        self.history.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        return response
    
    def ask_stream(self, prompt):

        self.history.append({
            "role": "user",
            "content": prompt,
        })

        chunks = []

        for token in self.brain.stream_chat(self.history):
            chunks.append(token)
            yield token

        self.history.append({
            "role": "assistant",
            "content": "".join(chunks)
        })

    def clear(self) -> None:
        self.history.clear()