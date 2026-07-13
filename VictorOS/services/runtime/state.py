from enum import Enum


class RuntimeState(str, Enum):

    IDLE = "idle"

    RUNNING = "running"

    BUSY = "busy"

    SHUTTING_DOWN = "shutting_down"