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

    def _build_plan(self, request: AssistantRequest) -> ExecutionPlan:
        """
        Build an execution plan from a user request.
        """

        task = self.classifier.classify(request.prompt)

        model = self.router.choose_model(task)

        return ExecutionPlan(
            prompt=request.prompt,
            task=task,
            model=model,
            agent="simple",
        )

    def handle(self, request: AssistantRequest) -> AssistantResponse:
        plan = self._build_plan(request)

        print(f"[Director] model = {plan.model}")

        result = self.runtime.run(plan)

        return AssistantResponse(
            content=result.summary,
            metadata={
                "execution": result,
                "model": plan.model,
                "task": plan.task.value,
            },
        )
    
    def submit(self, request: AssistantRequest):
        """
        Submit a request for background execution.

        Returns the Task object created by the Runtime.
        """

        plan = self._build_plan(request)

        print(f"[Director] submitted model = {plan.model}")

        return self.runtime.submit(plan)

    def dispatch(self, request: AssistantRequest):
        """
        Decide whether a request should execute
        immediately or in the background.
        """

        task = self.classifier.classify(request.prompt)

        background_tasks = {
            "coding",
            "research",
        }

        if task.value in background_tasks:
            return self.submit(request)

        return self.handle(request)