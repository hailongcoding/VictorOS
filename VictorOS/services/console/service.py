from VictorOS.core.base import BaseService


class ConsoleService(BaseService):

    def __init__(self):
        super().__init__("Console")

        self.logs = []

    def start(self):
        self.running = True
        print("[START] Console Service")

    def stop(self):
        self.running = False
        print("[STOP] Console Service")

    def write(self, message: str):

        self.logs.append(message)

    def history(self):

        return list(self.logs)

    def clear(self):

        self.logs.clear()