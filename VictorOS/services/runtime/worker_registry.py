from VictorOS.core.contracts.worker import Worker

class WorkerRegistry:

    def __init__(self):
        self._workers = {}

    def register(self, name: str, worker: Worker):
        self._workers[name] = worker

    def get(self, name: str) -> Worker:
        return self._workers[name]