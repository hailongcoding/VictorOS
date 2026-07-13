from typing import List

from .task import Task, TaskStatus


class TaskManager:

    def __init__(self):
        self.tasks: List[Task] = []

    def submit(self, task: Task):
        self.tasks.append(task)

    def all(self) -> List[Task]:
        return self.tasks

    def get(self, name: str) -> Task | None:
        for task in self.tasks:
            if task.name == name:
                return task
        return None

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

    def start(self, task: Task):
        task.status = TaskStatus.RUNNING

    def complete(self, task: Task, result: str):
        task.status = TaskStatus.COMPLETED
        task.result = result

    def fail(self, task: Task):
        task.status = TaskStatus.FAILED