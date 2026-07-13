from __future__ import annotations

from VictorOS.core.base import BaseService

class ServiceManager:

    def __init__(self):
        self._services: dict[str, BaseService] = {}

    def register(self, service: BaseService) -> None:
        self._services[service.name] = service

    def start_all(self) -> None:
        for service in self._services.values():
            service.start()

    def stop_all(self) -> None:
        for service in self._services.values():
            service.stop()

    def status(self) -> None:
        print("\nService Status")
        print("-" * 30)

        for service in self._services.values():
            print(f"{service.name:<15}{service.status()}")