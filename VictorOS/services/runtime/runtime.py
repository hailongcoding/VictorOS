
from .state import RuntimeState
from .context import RuntimeContext

from .event_bus import RuntimeEventBus
from .events import RuntimeEvent


class Runtime:

    def __init__(self, registry):
        self.bus = RuntimeEventBus()
        self.registry = registry
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
        self.context.current_worker = "default"

        try:
            worker = self.registry.get("default")
            response = worker.execute(plan)
            self.bus.publish(
                RuntimeEvent.TASK_COMPLETED,
                plan=plan,
                response=response
            )
            return response

        finally:
            self.context.state = RuntimeState.IDLE
            self.context.current_plan = None
            self.context.current_worker = None