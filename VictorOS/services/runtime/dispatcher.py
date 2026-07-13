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
        return self.registry.get("default")