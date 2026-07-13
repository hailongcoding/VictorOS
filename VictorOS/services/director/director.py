from __future__ import annotations

from openjarvis.learning.spec_search import plan

from VictorOS.contracts.assistant_request import AssistantRequest
from VictorOS.contracts.assistant_response import AssistantResponse
from VictorOS.services.brain.router import BrainRouter

from VictorOS.contracts.execution_plan import ExecutionPlan

from VictorOS.services.director.intent_classifier import IntentClassifier

from VictorOS.services.runtime.runtime_monitor import RuntimeMonitor

class Director:
    def __init__(
        self,
        router: BrainRouter,
        runtime,
    ):
        self.router = router
        self.runtime = runtime
        self.classifier = IntentClassifier()

        self.monitor = RuntimeMonitor(self.runtime.bus)

    def handle(self, request: AssistantRequest) -> AssistantResponse:
        task = self.classifier.classify(request.prompt)

        model = self.router.choose_model(task)

        plan = ExecutionPlan(
            prompt=request.prompt,
            task=task,
            model=model,
            agent="simple",
        )
        
        print(f"[Director] model = {model}")
        content = self.runtime.run(plan)

        return AssistantResponse(
            content=content,
            metadata={
                "model": model,
                "task": task.value,
            },
        )
    
    def submit(self, request: AssistantRequest):
        """
        Submit a request for background execution.

        Returns the Task object created by the Runtime.
        """

        task = self.classifier.classify(request.prompt)

        model = self.router.choose_model(task)

        plan = ExecutionPlan(
            prompt=request.prompt,
            task=task,
            model=model,
            agent="simple",
        )

        print(f"[Director] submitted model = {model}")

        return self.runtime.submit(plan)