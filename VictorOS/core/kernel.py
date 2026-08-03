
from __future__ import annotations
from VictorOS.core.config import ConfigManager
from VictorOS.core.events import EventBus
from VictorOS.core.manager import ServiceManager

from VictorOS.core.message_bus import MessageBus

import time

from VictorOS.services.capabilities.registry import CapabilityRegistry
from VictorOS.services.capabilities.provider import CapabilityProvider

from VictorOS.services.providers.gateway import ProviderGateway

from VictorOS.services.brain.adapter import OllamaAdapter
from VictorOS.services.brain.service import BrainService
from VictorOS.services.brain.session import ChatSession

from VictorOS.core.contracts.assistant_request import AssistantRequest
from VictorOS.core.contracts.execution_request import ExecutionRequest
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

from VictorOS.core.planner.service import PlannerService
from VictorOS.core.planner.adapter import PlannerAdapter

from VictorOS.services.runtime.request_factory import ExecutionRequestFactory

from VictorOS.services.reasoning.service import ReasoningService
from VictorOS.services.reasoning.dummy_adapter import DummyReasoningAdapter

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

    def plan(self, prompt):

        return self.planner.plan(prompt)
            
    
    def execute(
        self,
        prompt: str,
    ):

        understanding = self.intent.understand(prompt)

        print("\n========== UNDERSTANDING ==========")
        print(understanding)

        print("\n========== UNDERSTANDING 2 ==========")
        print(f"Goal       : {understanding.goal}")
        print(f"Confidence : {understanding.confidence}")

        print("\nEntities:")
        for entity in understanding.entities:
            print(f"  • {entity}")

        print("\nIntents:")
        for intent in understanding.intents:
            print(f"  Goal : {intent.goal}")
            print(f"  Desc : {intent.description}")

        reasoning = self.reasoning.reason(
            understanding
        )

        print("\n========== REASONING ==========")

        for decision in reasoning.decisions:
            print(f"Capability : {decision.capability}")
            print(f"Confidence : {decision.confidence}")
            print(f"Reason     : {decision.reason}")
            print()

        requests = []

        for decision in reasoning.decisions:

            requests.append(
                self.request_factory.create(
                    decision
                )
            )

        print("\n========== EXECUTION REQUESTS ==========")

        for request in requests:
            print(request)

        results = []

        for request in requests:

            results.append(
                self.runtime.run(request)
            )

        print("\n========== RESULTS ==========")

        for result in results:
            print(result)

        return results

    def boot(self) -> None:
        print("=" * 40)
        print("        VictorOS v0.1")
        print("=" * 40)
        self.config.load()

        self.capabilities = CapabilityRegistry()

        self.request_factory = ExecutionRequestFactory()

        from VictorOS.services.ai.client import AIClient

        self.ai_client = AIClient()

        planner_adapter = PlannerAdapter(
            self.ai_client
        )

        self.planner = PlannerService(
            planner_adapter,
            self.capabilities,
        )

        self.console_service = ConsoleService()

        self.console = ConsoleController(
            self.console_service
        )

        self.gateway = ProviderGateway(
            self.capabilities,
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

        from VictorOS.services.intent.service import IntentService

        self.intent = IntentService()

        self.reasoning = ReasoningService(
            DummyReasoningAdapter()
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

            # intent = self.intent.classify(prompt)

            # print(f"[Intent] {intent}")



            # decision = self.captain.handle(prompt)

            # print(f"Captain > {decision.reply}")

            # if not decision.use_brain:
            #     print()
                

            # print("Thinking...")

            # response = self.processor.process(prompt)
            # if hasattr(response, "content"):
            #     print(f"Brain > {response.content}")
            results = self.execute(prompt)

            print(results)
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