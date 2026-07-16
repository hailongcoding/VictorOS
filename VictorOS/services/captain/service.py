from .decision import CaptainDecision
from VictorOS.core.base import BaseService
from .responses import (
    TASK_STARTED,
    TASK_COMPLETED,
    TASK_FAILED,
    GREETINGS,
    random_response,
)

class CaptainService(BaseService):

    def __init__(self, adapter):
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

    # -------------------------
    # Captain API
    # -------------------------

    def acknowledge(self, plan):

        return random_response(TASK_STARTED)


    def task_started(self, task):

        return f"{task.name.capitalize()} started."

    def task_completed(self, task, result):

        return random_response(TASK_COMPLETED)


    def task_failed(self, task, error):

        return random_response(TASK_FAILED)

        return f"{task.name.capitalize()} failed."

    def notify(
        self,
        message,
    ):

        return message

    def handle(self, prompt: str):

        text = prompt.lower().strip()

        greetings = {
            "hi",
            "hello",
            "hey",
            "yo",
            "yoo",
            "yoo hoo",
        }

        if text in greetings:

            return CaptainDecision(
                handled=True,
                response="Hello."
            )

        if text in ("thanks", "thank you"):

            return CaptainDecision(
                handled=True,
                response="You're welcome."
            )

        return CaptainDecision(
            handled=False
        )