from VictorOS.services.notifications.service import NotificationService
from VictorOS.services.notifications.controller import NotificationController
from VictorOS.services.notifications.notification import (
    Notification,
    NotificationLevel,
)

from VictorOS.services.task_manager import task
from VictorOS.services.task_manager.manager import TaskManager

from VictorOS.services.task_manager.controller import TaskController

from VictorOS.services.task_manager.task import Task

from .state import RuntimeState
from .context import RuntimeContext

from .event_bus import RuntimeEventBus
from .events import RuntimeEvent

from VictorOS.services.runtime.dispatcher import Dispatcher

from VictorOS.services.runtime.background_worker import BackgroundWorker


class Runtime:

    def __init__(self, registry):
        self.bus = RuntimeEventBus()
        self.registry = registry
        self.dispatcher = Dispatcher(registry)
        self.task_manager = TaskManager()

        self.tasks = TaskController(
            self.task_manager
        )
        
        notification_service = NotificationService()

        self.notifications = NotificationController(
            notification_service
        )

        self.context = RuntimeContext(
            state=RuntimeState.IDLE
        )

    def run(self, plan):

        self.context.state = RuntimeState.RUNNING
        self.bus.publish(
            RuntimeEvent.TASK_STARTED,
            plan=plan
        )
        self.context.current_plan = plan
        task = Task(
            name=plan.task.value,
            payload=plan,
        )

        self.tasks.submit(task)

        self.tasks.start(task.id)

        self.notifications.send(
            Notification(
                title="Task Started",
                message=f"{task.name} started.",
                level=NotificationLevel.INFO,
            )
        )

        self.context.current_worker = "default"

        try:
            return self._execute(plan, task)

        except Exception:
            self.tasks.fail(task.id)

            self.notifications.send(
                Notification(
                    title="Task Failed",
                    message=f"{task.name} failed.",
                    level=NotificationLevel.ERROR,
                )
            )

            raise
        
        finally:
            self.context.state = RuntimeState.IDLE
            self.context.current_plan = None
            self.context.current_worker = None

    def submit(self, plan):
        """
        Execute a plan in the background.

        Returns the Task immediately.
        """

        task = Task(
            name=plan.task.value,
            payload=plan,
        )

        self.tasks.submit(task)

        worker = BackgroundWorker(
            self._run_background,
            plan,
            task,
        )

        worker.start()

        return task

    def _run_background(self, plan, task):

        self.tasks.start(task.id)

        self.notifications.send(
            Notification(
                title="Task Started",
                message=f"{task.name} started.",
                level=NotificationLevel.INFO,
            )
        )

        self.context.state = RuntimeState.RUNNING
        self.context.current_plan = plan
        self.context.current_worker = "default"

        self.bus.publish(
            RuntimeEvent.TASK_STARTED,
            plan=plan,
        )

        try:
            response = self._execute(plan, task)

        except Exception:

            self.tasks.fail(task.id)

            self.notifications.send(
                Notification(
                    title="Task Failed",
                    message=f"{task.name} failed.",
                    level=NotificationLevel.ERROR,
                )
            )

            raise

        finally:

            self.context.state = RuntimeState.IDLE
            self.context.current_plan = None
            self.context.current_worker = None

    def _execute(self, plan, task):

        worker = self.dispatcher.dispatch(plan)

        response = worker.execute(plan)

        self.tasks.complete(
            task.id,
            response,
        )

        self.notifications.send(
            Notification(
                title="Task Completed",
                message=f"{task.name} completed.",
                level=NotificationLevel.SUCCESS,
            )
        )

        self.bus.publish(
            RuntimeEvent.TASK_COMPLETED,
            plan=plan,
            response=response
        )

        return response