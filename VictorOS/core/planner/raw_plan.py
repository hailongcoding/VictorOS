from dataclasses import dataclass


@dataclass(slots=True)
class RawTask:
    goal: str
    capabilities: list[str]


@dataclass(slots=True)
class RawPlan:
    tasks: list[RawTask]