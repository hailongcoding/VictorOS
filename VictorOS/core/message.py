from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Message:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    sender: str = ""

    receiver: str = ""

    type: str = ""

    payload: dict = field(default_factory=dict)

    created_at: datetime = field(default_factory=datetime.utcnow)