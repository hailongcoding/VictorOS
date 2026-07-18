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
        
    def respond(self, decision):

        messages = [
            {
                "role": "system",
                "content": (
                    "You are Captain, the executive AI of VictorOS.\n"
                    "You are the FIRST personality users interact with.\n"
                    "Reply naturally, briefly and confidently.\n"
                    "Never say you are OpenJarvis.\n"
                    "Never mention models or AI architecture.\n"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Intent: {decision.intent.name}\n"
                    f"User: {decision.original_prompt}"
                ),
            },
        ]

        return self.speak(messages)

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

        return self.adapter.handle(prompt)
