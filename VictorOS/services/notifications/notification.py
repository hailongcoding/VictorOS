from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class NotificationLevel(str, Enum):
    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


@dataclass
class Notification:
    title: str
    message: str

    level: NotificationLevel = NotificationLevel.INFO

    created_at: datetime = field(default_factory=datetime.now)

    read: bool = False