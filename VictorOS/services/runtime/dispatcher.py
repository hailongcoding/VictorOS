from VictorOS.services.runtime.worker_registry import WorkerRegistry


class Dispatcher:

    def __init__(self, registry: WorkerRegistry):
        self.registry = registry

    def dispatch(self, plan):
        """
        Decide which worker should execute this plan.

        For now, everything uses the default worker.
        Future versions will route coding, research,
        automation, desktop control, etc.
        """
        task_name = plan.task.value.lower()

        if task_name == "conversation":
            worker_name = "conversation"

        elif task_name == "coding":
            worker_name = "coding"

        elif task_name == "research":
            worker_name = "research"

        else:
            worker_name = "default"

        return self.registry.get(worker_name)