from dataclasses import dataclass

from VictorOS.core.contracts.execution_plan import ExecutionPlan

from .state import RuntimeState


@dataclass
class RuntimeContext:

    state: RuntimeState

    current_plan: ExecutionPlan | None = None

    current_worker: str | None = None