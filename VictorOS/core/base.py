from __future__ import annotations

from abc import ABC, abstractmethod


class BaseService(ABC):
    """Base class for every JarvisOS service."""

    def __init__(self, name: str):
        self.name = name
        self.running = False

    @abstractmethod
    def start(self) -> None:
        ...

    @abstractmethod
    def stop(self) -> None:
        ...

    def restart(self) -> None:
        self.stop()
        self.start()

    def status(self) -> str:
        return "Running" if self.running else "Stopped"