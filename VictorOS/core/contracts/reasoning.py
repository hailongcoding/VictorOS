from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from VictorOS.core.contracts.understanding import Understanding

@dataclass(slots=True)
class Decision:
    """
    One reasoning decision.

    Decides WHAT VictorOS should accomplish
    and WHICH capability should accomplish it.
    """

    goal: str

    capability: str

    confidence: float

    reason: str

    payload: dict[str, Any] = field(default_factory=dict)

@dataclass(slots=True)
class Reasoning:
    """
    Output of the reasoning stage.

    Produced from an Understanding object.
    """

    understanding: Understanding

    decisions: list[Decision]

    metadata: dict[str, Any] = field(default_factory=dict)