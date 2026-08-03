from __future__ import annotations


from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

@dataclass(slots=True)
class ExecutionRequest:

    capability: str

    payload: Any

    background: bool = False

    metadata: dict[str, Any] = field(default_factory=dict)