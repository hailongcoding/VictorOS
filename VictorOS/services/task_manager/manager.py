from typing import List

from .task import Task, TaskStatus


class TaskManager:

    def __init__(self):
        self.tasks: List[Task] = []

    def submit(self, task: Task):
        self.tasks.append(task)

    def all(self) -> List[Task]:
        return self.tasks

    def get_by_name(self, name: str) -> Task | None:
        for task in self.tasks:
            if task.name == name:
                return task
        return None

    def get(self, task_id: int) -> Task | None:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
        
    def exists(self, task_id: int) -> bool:
        return self.get(task_id) is not None

    def queued(self):
        return [
            t for t in self.tasks
            if t.status == TaskStatus.QUEUED
        ]

    def running(self):
        return [
            t for t in self.tasks
            if t.status == TaskStatus.RUNNING
        ]

    def completed(self):
        return [
            t for t in self.tasks
            if t.status == TaskStatus.COMPLETED
        ]

    def failed(self):
        return [
            t for t in self.tasks
            if t.status == TaskStatus.FAILED
        ]

    def by_status(self, status: TaskStatus):
        return [
            task
            for task in self.tasks
            if task.status == status
        ]

    def active(self):
        return [
            t for t in self.tasks
            if t.status in (
                TaskStatus.QUEUED,
                TaskStatus.RUNNING,
            )
        ]

    def start(self, task: Task):
        task.status = TaskStatus.RUNNING

    def complete(self, task: Task, result: str):
        task.status = TaskStatus.COMPLETED
        task.result = result

    def fail(self, task: Task):
        task.status = TaskStatus.FAILED

    def cancel(self, task: Task):
        task.status = TaskStatus.CANCELLED