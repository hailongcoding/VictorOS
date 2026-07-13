from VictorOS.services.task_manager.manager import TaskManager
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

        self.task_manager.submit(task)
        self.task_manager.start(task)
        self.context.current_worker = "default"

        try:
            return self._execute(plan, task)

        except Exception:
            self.task_manager.fail(task)
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

        self.task_manager.submit(task)

        worker = BackgroundWorker(
            self._run_background,
            plan,
            task,
        )

        worker.start()

        return task

    def _run_background(self, plan, task):

        self.task_manager.start(task)

        self.bus.publish(
            RuntimeEvent.TASK_STARTED,
            plan=plan,
        )

        try:
            response = self._execute(plan, task)

        except Exception:

            self.task_manager.fail(task)

            raise

        finally:

            self.context.state = RuntimeState.IDLE

    def _execute(self, plan, task):

        worker = self.dispatcher.dispatch(plan)

        response = worker.execute(plan)

        self.task_manager.complete(task, response)

        self.bus.publish(
            RuntimeEvent.TASK_COMPLETED,
            plan=plan,
            response=response
        )

        return response