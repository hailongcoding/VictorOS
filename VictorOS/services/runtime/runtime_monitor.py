from .events import RuntimeEvent


class RuntimeMonitor:

    def __init__(self, bus):
        self.bus = bus

        self.bus.subscribe(
            RuntimeEvent.TASK_STARTED,
            self.on_task_started
        )

        self.bus.subscribe(
            RuntimeEvent.TASK_COMPLETED,
            self.on_task_completed
        )

    def on_task_started(self, plan):
        print(f"[Runtime] Started: {plan.task.value}")

    def on_task_completed(self, plan, response):
        print(f"[Runtime] Completed: {plan.task.value}")