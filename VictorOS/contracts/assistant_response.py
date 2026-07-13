from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AssistantResponse:
    content: str
    success: bool = True
    metadata: dict[str, Any] = field(default_factory=dict)