
from __future__ import annotations
from urllib import response
from VictorOS.core.config import ConfigManager
from VictorOS.core.events import EventBus
from VictorOS.core.manager import ServiceManager

import time

from VictorOS.services.brain.adapter import OllamaAdapter
from VictorOS.services.brain.service import BrainService
from VictorOS.services.brain.session import ChatSession

from VictorOS.contracts.assistant_request import AssistantRequest
from VictorOS.services.director.director import Director

from VictorOS.services.command.processor import CommandProcessor

from VictorOS.services.brain.tasks import BrainTask
from VictorOS.services.brain.router import BrainRouter

from VictorOS.services.listener.listener import JarvisListener

from VictorOS.services.executor.executor import Executor

from VictorOS.services.runtime.runtime import Runtime
from VictorOS.services.runtime.worker_registry import WorkerRegistry
from VictorOS.services.runtime.default_worker import DefaultWorker

class Kernel:
    """Central runtime of JarvisOS."""

    def __init__(self) -> None:
        from pathlib import Path
        self.listener = JarvisListener()

        BASE_DIR = Path(__file__).resolve().parent.parent

        self.config = ConfigManager(
            BASE_DIR / "config" / "settings.toml"
        )
        self.events = EventBus()
        self.manager = ServiceManager()

        # Services
        self.brain = None

    def boot(self) -> None:
        print("=" * 40)
        print("        VictorOS v0.1")
        print("=" * 40)

        self.config.load()
#        adapter = OllamaAdapter(
#            model=config.get("brain.default_model"),
#            host=self.config.get("brain.host"),
#        )
        from VictorOS.services.brain.openjarvis_adapter import OpenJarvisAdapter

        adapter = OpenJarvisAdapter()

        self.brain = BrainService(adapter=adapter)
        self.executor = Executor(self.brain)

        registry = WorkerRegistry()

        default_worker = DefaultWorker(self.executor)

        registry.register(
            "default",
            default_worker,
        )

        registry.register(
            "conversation",
            default_worker,
        )

        registry.register(
            "coding",
            default_worker,
        )

        registry.register(
            "research",
            default_worker,
        )

        self.runtime = Runtime(registry)
        
        self.router = BrainRouter(self.config)

        self.director = Director(
            router=self.router,
            runtime=self.runtime,
        )

        self.processor = CommandProcessor(self.director)

        self.events.subscribe(
            "system.boot",
            lambda message: print(f"[EVENT] {message}")
        )

        self.manager.register(self.brain)

        self.events.publish(
            "system.boot",
            "Kernel Boot Complete"
        )

        print()

        self.manager.start_all()

        print()

        self.manager.status()

        print()

        print(f"Theme : {self.config.get('ui.theme')}")

        print("\nType 'exit' to quit.\n")

        self.listener.start()

        while True:

            prompt = input("You > ").strip()

            if not prompt:
                continue

            if prompt.lower() in ("exit", "quit"):
                break

            print("Thinking...")


            start = time.perf_counter()

            response = self.processor.process(prompt)
            
            if hasattr(response, "content"):
                print(f"Brain > {response.content}")
            else:
                print(response)

            elapsed = time.perf_counter() - start

            print()
            
        self.listener.stop()

        self.shutdown()

    def shutdown(self) -> None:
        print()
        print("[EVENT] Shutting down...")
        self.manager.stop_all()

        print("Goodbye!")