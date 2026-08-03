from abc import ABC, abstractmethod


class AIProvider(ABC):

    @abstractmethod
    def chat(
        self,
        *,
        model: str,
        messages: list[dict],
        stream: bool = False,
        think: bool = False,
    ) -> str:
        pass