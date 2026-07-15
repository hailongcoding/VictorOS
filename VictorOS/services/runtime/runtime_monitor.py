from .events import RuntimeEvent

from .event_data import RuntimeEventData

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

        self.bus.subscribe(
            RuntimeEvent.TASK_FAILED,
            self.on_task_failed,
        )

    def on_task_started(self, data: RuntimeEventData):
        print(f"[Runtime] Started: {data.task.name}")
    def on_task_completed(self, data: RuntimeEventData):
        print(f"[Runtime] Completed: {data.task.name}")
    def on_task_failed(self, data: RuntimeEventData):
        print(f"[Runtime] Failed: {data.task.name}")