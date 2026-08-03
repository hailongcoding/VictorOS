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

from VictorOS.services.runtime.events import RuntimeEvent

from VictorOS.services.runtime.event_data import RuntimeEventData


class Runtime:

    def __init__(self, registry, bus):
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

    def run(self, request):

        self.context.state = RuntimeState.RUNNING

        task = Task(
            name=request.capability,
            payload=request,
        )

        self.tasks.submit(task)

        self.tasks.start(task.id)

        self.bus.publish(
            RuntimeEvent.TASK_STARTED,
            data=RuntimeEventData(
                task=task,
            )
        )

        self.notifications.send(
            Notification(
                title="Task Started",
                message=f"{task.name} started.",
                level=NotificationLevel.INFO,
            )
        )

        self.context.current_worker = "default"

        try:
            return self._execute(request, task)

        except Exception as e:

            self.tasks.fail(task.id)

            self.bus.publish(
                RuntimeEvent.TASK_FAILED,
                data=RuntimeEventData(
                    task=task,
                    error=e,
                )
            )

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

    def submit(self, request):
        """
        Execute a request in the background.

        Returns the Task immediately.
        """

        task = Task(
            name=request.capability,
            payload=request,
        )

        self.tasks.submit(task)

        worker = BackgroundWorker(
            self._run_background,
            request,
            task,
        )

        worker.start()

        return task

    def _run_background(self, request, task):

        self.tasks.start(task.id)

        self.notifications.send(
            Notification(
                title="Task Started",
                message=f"{task.name} started.",
                level=NotificationLevel.INFO,
            )
        )

        self.context.state = RuntimeState.RUNNING
        self.context.current_request = request
        self.context.current_worker = "default"

        self.bus.publish(
            RuntimeEvent.TASK_STARTED,
            data=RuntimeEventData(
                task=task,
            )
        )

        try:
            response = self._execute(request, task)

        except Exception as e:

            self.tasks.fail(task.id)

            self.bus.publish(
                RuntimeEvent.TASK_FAILED,
                data=RuntimeEventData(
                    task=task,
                    error=e,
                )
            )

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
            self.context.current_request = None
            self.context.current_worker = None

    def _execute(self, request, task):

        worker = self.dispatcher.dispatch(request)

        self.tasks.set_progress(
            task.id,
            10,
            "Starting worker",
        )

        result = worker.execute(request)

        self.tasks.set_progress(
            task.id,
            90,
            "Finalizing",
        )

        self.tasks.complete(
            task.id,
            result,
        )

        self.tasks.set_progress(
            task.id,
            100,
            "Completed",
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
            data=RuntimeEventData(
                task=task,
                response=result,
            )
        )
        return result