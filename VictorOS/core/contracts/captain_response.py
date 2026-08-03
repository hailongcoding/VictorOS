from dataclasses import dataclass, field


@dataclass
class CaptainResponse:

    action: str

    reply: str

    use_brain: bool = False

    worker: str | None = None

    metadata: dict = field(default_factory=dict)