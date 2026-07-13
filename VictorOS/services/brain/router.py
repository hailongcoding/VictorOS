from __future__ import annotations

from VictorOS.core.config import ConfigManager

from VictorOS.services.brain.tasks import BrainTask
class BrainRouter:
    def __init__(self, config: ConfigManager):
        self.config = config

    def conversation_model(self) -> str:
        return self.config.get("brain.conversation_model")

    def reasoning_model(self) -> str:
        return self.config.get("brain.reasoning_model")

    def coding_model(self) -> str:
        return self.config.get("brain.coding_model")

    def research_model(self) -> str:
        return self.config.get("brain.research_model")

    def default_model(self) -> str:
        return self.config.get("brain.default_model")

    def choose_model(self, task: BrainTask) -> str:
        print(f"[Router] Task = {task}")
        if task == BrainTask.CONVERSATION:
            print(f"[Router] Task = {task}")
            return self.conversation_model()

        if task == BrainTask.CODING:
            print(f"[Router] Task = {task}")
            return self.coding_model()

        if task == BrainTask.REASONING:
            print(f"[Router] Task = {task}")
            return self.reasoning_model()

        if task == BrainTask.RESEARCH:
            print(f"[Router] Task = {task}")
            return self.research_model()

        return self.default_model()