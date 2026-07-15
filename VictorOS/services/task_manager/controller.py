from .manager import TaskManager
from .task import TaskStatus


class TaskController:

    def __init__(self, manager: TaskManager):
        self.manager = manager

    def list(self):
        return self.manager.all()

    def active(self):
        return self.manager.active()

    def completed(self):
        return self.manager.completed()

    def failed(self):
        return self.manager.failed()
    
    def start(self, task_id: int):

        task = self.manager.get(task_id)

        if task is None:
            return False

        self.manager.start(task)

        return True

    def complete(
        self,
        task_id: int,
        result: str,
    ):

        task = self.manager.get(task_id)

        if task is None:
            return False

        self.manager.complete(
            task,
            result,
        )

        return True

    def fail(self, task_id: int):

        task = self.manager.get(task_id)

        if task is None:
            return False

        self.manager.fail(task)

        return True

    def submit(self, task):

        self.manager.submit(task)

        return task

    def cancel(self, task_id: int):

        task = self.manager.get(task_id)

        if task is None:
            return False

        if task.status in (
            TaskStatus.COMPLETED,
            TaskStatus.FAILED,
            TaskStatus.CANCELLED,
        ):
            return False

        self.manager.cancel(task)

        return True

    def status(self, task_id: int):

        task = self.manager.get(task_id)

        if task is None:
            return None

        return task.status

    def result(self, task_id: int):

        task = self.manager.get(task_id)

        if task is None:
            return None

        return task.result

    def set_progress(
        self,
        task_id: int,
        progress: int,
        step: str,
    ):
        task = self.manager.get(task_id)

        if task is None:
            return

        task.progress = progress
        task.current_step = step