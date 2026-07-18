
from __future__ import annotations
from VictorOS.core.config import ConfigManager
from VictorOS.core.events import EventBus
from VictorOS.core.manager import ServiceManager

from VictorOS.core.message_bus import MessageBus

import time

from VictorOS.services.capabilities.registry import CapabilityRegistry
from VictorOS.services.capabilities.provider import CapabilityProvider

from VictorOS.services.intelligence.gateway import IntelligenceGateway

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

from VictorOS.services.console.service import ConsoleService
from VictorOS.services.console.controller import ConsoleController

from VictorOS.services.plugins.manager import PluginManager

from VictorOS.services.runtime.events import RuntimeEvent

from VictorOS.services.captain.adapter import CaptainAdapter
from VictorOS.services.captain.service import CaptainService

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
        self.bus = MessageBus()
        self.manager = ServiceManager()

        # Services
        self.brain = None

    def boot(self) -> None:
        print("=" * 40)
        print("        VictorOS v0.1")
        print("=" * 40)

        self.config.load()

        self.console_service = ConsoleService()

        self.console = ConsoleController(
            self.console_service
        )

        self.capabilities = CapabilityRegistry()

        self.gateway = IntelligenceGateway(
            self.capabilities
        )

#        adapter = OllamaAdapter(
#            model=config.get("brain.default_model"),
#            host=self.config.get("brain.host"),
#        )
        bus = self.bus

#        bus.subscribe(
#            "captain",
#            self.captain.receive
#        )
#
#        bus.subscribe(
#            "brain",
#            self.brain.receive
#        )
#
#        bus.subscribe(
#            "runtime",
#            self.runtime.receive
#        )

        from VictorOS.services.brain.openjarvis_adapter import OpenJarvisAdapter

        adapter = OpenJarvisAdapter()

        from VictorOS.services.plugins.manager import PluginManager

        self.plugins = PluginManager()
        self.plugins.register(adapter)

        self.brain = BrainService(adapter=adapter)

        captain_adapter = CaptainAdapter()

        self.captain = CaptainService(
            captain_adapter
        )


        for provider in self.plugins.all():

            manifest = provider.get_manifest()

            for capability in manifest.capabilities:
                self.capabilities.register(
                    CapabilityProvider(
                        name=manifest.name,
                        capability=capability,
                        implementation=provider,
                        priority=manifest.priority,
                    )
                )

            self.console.info(
                f"Registered {manifest.name}",
                source="Kernel",
            )

        self.executor = Executor(
            self.gateway
        )

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

        self.runtime = Runtime(
            registry,
            self.bus,
        )

#        self.runtime.bus.subscribe(
#            RuntimeEvent.TASK_COMPLETED,
#            lambda data: self.captain.task_completed(
#                data.response
#            )
#        )


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

        self.runtime.bus.subscribe(
            RuntimeEvent.TASK_STARTED,
            lambda data: self.console.info(
                f"Task started: {data.task.name}",
                source="Runtime",
            )
        )

        self.runtime.bus.subscribe(
            RuntimeEvent.TASK_COMPLETED,
            lambda data: self.console.info(
                f"Task completed: {data.task.name}",
                source="Runtime",
            )
        )

        self.runtime.bus.subscribe(
            RuntimeEvent.TASK_FAILED,
            lambda data: self.console.info(
                f"Task failed: {data.task.name}",
                source="Runtime",
            )
        )

        self.manager.register(self.brain)
        self.manager.register(self.captain)
        self.manager.register(self.console_service)

        self.events.publish(
            "system.boot",
            "Kernel Boot Complete"
        )
        
        self.console.info(
            "Kernel boot complete",
            source="Kernel",
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

   



            decision = self.captain.handle(prompt)

            print(f"Captain > {decision.reply}")

            if not decision.use_brain:
                print()
                

            print("Thinking...")

            response = self.processor.process(prompt)
            if hasattr(response, "content"):
                print(f"Brain > {response.content}")
            print()
            
        self.listener.stop()

        self.shutdown()

    def shutdown(self) -> None:
        print()
        print("[EVENT] Shutting down...")

        self.console.info(
            "VictorOS shutting down",
            source="Kernel",
        )

        self.manager.stop_all()

        print("Goodbye!")