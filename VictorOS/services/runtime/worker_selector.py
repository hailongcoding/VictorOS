from JarvisOS.contracts.execution_plan import ExecutionPlan
from JarvisOS.services.runtime.worker_registry import WorkerRegistry


class WorkerSelector:

    def __init__(self, registry: WorkerRegistry):
        self.registry = registry

    def select(self, plan: ExecutionPlan):
        # Temporary implementation.
        # Everything uses the default worker for now.
        return self.registry.get("default")