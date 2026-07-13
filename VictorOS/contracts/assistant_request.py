from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from VictorOS.services.brain.tasks import BrainTask


@dataclass
class AssistantRequest:
    prompt: str
    task: BrainTask
    source: str = "terminal"
    metadata: dict[str, Any] = field(default_factory=dict)