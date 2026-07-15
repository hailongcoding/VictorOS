from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExecutionResult:
    success: bool
    summary: str

    files_created: list[str] = field(default_factory=list)
    files_modified: list[str] = field(default_factory=list)

    artifacts: list[str] = field(default_factory=list)

    actions: list[str] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

    suggestions: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

    