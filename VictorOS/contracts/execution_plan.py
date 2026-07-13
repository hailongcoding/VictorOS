from dataclasses import dataclass, field

from VictorOS.services.brain.tasks import BrainTask


@dataclass
class ExecutionPlan:
    prompt: str

    task: BrainTask

    model: str

    agent: str

    tools: list[str] = field(default_factory=list)

    stream: bool = True

    background: bool = False