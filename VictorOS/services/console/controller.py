from .service import ConsoleService


class ConsoleController:

    def __init__(self, service: ConsoleService):
        self.service = service

    def log(
        self,
        message: str,
        level: str = "INFO",
        source: str = "VictorOS",
    ):

        self.service.write(
            message,
            level=level,
            source=source,
        )

    def info(
        self,
        message: str,
        source: str = "VictorOS",
    ):

        self.log(
            message,
            level="INFO",
            source=source,
        )

    def warning(
        self,
        message: str,
        source: str = "VictorOS",
    ):

        self.log(
            message,
            level="WARNING",
            source=source,
        )

    def error(
        self,
        message: str,
        source: str = "VictorOS",
    ):

        self.log(
            message,
            level="ERROR",
            source=source,
        )

    def debug(
        self,
        message: str,
        source: str = "VictorOS",
    ):

        self.log(
            message,
            level="DEBUG",
            source=source,
        )

    def history(self):

        return self.service.history()

    def latest(self, limit=20):

        return self.service.latest(limit)

    def clear(self):

        self.service.clear()