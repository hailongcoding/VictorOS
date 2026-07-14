from VictorOS.core.base import BaseService
from VictorOS.services.brain.adapter import BrainAdapter


class BrainService(BaseService):



    def __init__(self, adapter: BrainAdapter):
        super().__init__("Brain")
        self.adapter = adapter

    def start(self) -> None:
        self.running = True
        print("[START] Brain Service")

    def stop(self) -> None:
        self.running = False
        print("[STOP] Brain Service")

    def chat(
        self,
        messages: list[dict[str, str]],
        model=None

    ) -> str:
        return self.adapter.chat(messages,model=model)
    
    def stream_chat(self, messages):
        return self.adapter.stream_chat(messages)