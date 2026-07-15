from enum import Enum


class ProviderStatus(str, Enum):

    ONLINE = "online"

    OFFLINE = "offline"

    DISABLED = "disabled"

    ERROR = "error"