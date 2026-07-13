from VictorOS.services.executor.executor import Executor
from VictorOS.services.runtime.worker import Worker


class DefaultWorker(Worker):

    def __init__(self, executor: Executor):
        self.executor = executor

    def execute(self, plan):
        return self.executor.execute(plan)