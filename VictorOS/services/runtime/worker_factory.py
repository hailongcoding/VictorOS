from JarvisOS.services.runtime.default_worker import DefaultWorker


class WorkerFactory:

    def __init__(self, executor):
        self.executor = executor

    def create(self, task):

        return DefaultWorker(self.executor)