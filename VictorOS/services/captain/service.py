from VictorOS.core.base import BaseService

from .adapter import CaptainAdapter


class CaptainService(BaseService):

    def __init__(self, adapter: CaptainAdapter):
        super().__init__("Captain")
        self.adapter = adapter

    def start(self):
        self.running = True
        print("[START] Captain Service")

    def stop(self):
        self.running = False
        print("[STOP] Captain Service")

    def speak(
        self,
        messages,
        model=None,
    ):
        return self.adapter.chat(
            messages,
            model=model,
        )