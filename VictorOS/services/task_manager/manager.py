from typing import List

from .task import Task, TaskStatus
from services.task_manager import task


class TaskManager:
    def __init__(self):
        self.tasks: List[Task] = []

    def submit(self, task: Task):
        self.tasks.append(task)

    def running(self):
        return [t for t in self.tasks if t.status == "running"]

    def queued(self):
        return [t for t in self.tasks if t.status == "queued"]

    def completed(self):
        return [
            t for t in self.tasks
            if t.status == TaskStatus.COMPLETED
        ]
    
    def fail(self, task: Task):
        task.status = TaskStatus.FAILED