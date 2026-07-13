from openjarvis import Jarvis


class OpenJarvisAdapter:
    def __init__(self):
        self.jarvis = Jarvis()

    def ask(self, prompt: str) -> str:
        return self.jarvis.ask(prompt)

    def close(self):
        self.jarvis.close()