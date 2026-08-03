from VictorOS.services.runtime.worker_registry import WorkerRegistry


class Dispatcher:

    def __init__(self, registry: WorkerRegistry):
        self.registry = registry

    def dispatch(self, request):
        """
        Decide which worker should execute this plan.

        For now, everything uses the default worker.
        Future versions will route coding, research,
        automation, desktop control, etc.
        """
        capability = request.capability.lower()

        if capability == "conversation":
            worker_name = "conversation"

        elif capability ==  "coding":
            worker_name = "coding"

        elif capability ==  "research":
            worker_name = "research"

        else:
            worker_name = "default"

        return self.registry.get(worker_name)