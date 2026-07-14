from .service import ConsoleService


class ConsoleController:

    def __init__(self, service: ConsoleService):
        self.service = service

    def log(self, message: str):

        self.service.write(message)

    def history(self):

        return self.service.history()

    def clear(self):

        self.service.clear()