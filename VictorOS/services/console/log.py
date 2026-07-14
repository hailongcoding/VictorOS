from dataclasses import dataclass
from datetime import datetime


@dataclass
class ConsoleLog:
    timestamp: datetime
    level: str
    source: str
    message: str