from enum import Enum, auto


class RuntimeEvent(Enum):
    TASK_STARTED = auto()
    TASK_COMPLETED = auto()
    TASK_FAILED = auto()