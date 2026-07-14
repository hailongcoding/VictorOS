from VictorOS.core.base import BaseService

from datetime import datetime

from .log import ConsoleLog

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

    def write(
        self,
        message: str,
        level: str = "INFO",
        source: str = "VictorOS",
    ):

        self.logs.append(
            ConsoleLog(
                timestamp=datetime.now(),
                level=level,
                source=source,
                message=message,
            )
        )

    def history(self):

        return list(self.logs)
    
    def latest(self, limit: int = 20):

        return self.logs[-limit:]

    def clear(self):

        self.logs.clear()