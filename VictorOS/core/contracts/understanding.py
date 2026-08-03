from dataclasses import dataclass, field


@dataclass(slots=True)
class Intent:

    goal: str

    description: str

    entities: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Understanding:

    original: str

    goal: str

    confidence: float

    intents: list[Intent] = field(default_factory=list)

    entities: list[str] = field(default_factory=list)

    metadata: dict = field(default_factory=dict)