from VictorOS.services.task_manager.manager import TaskManager
from VictorOS.services.task_manager.task import Task

from .state import RuntimeState
from .context import RuntimeContext

from .event_bus import RuntimeEventBus
from .events import RuntimeEvent


class Runtime:

    def __init__(self, registry):
        self.bus = RuntimeEventBus()
        self.registry = registry
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
            worker = self.registry.get("default")
            response = worker.execute(plan)
            self.task_manager.complete(task, response)
            self.bus.publish(
                RuntimeEvent.TASK_COMPLETED,
                plan=plan,
                response=response
            )
            return response
        except Exception:

            self.task_manager.fail(task)
            raise
        
        finally:
            self.context.state = RuntimeState.IDLE
            self.context.current_plan = None
            self.context.current_worker = None