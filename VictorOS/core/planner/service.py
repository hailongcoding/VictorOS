from VictorOS.core.planner.parser import PlannerParser

from VictorOS.core.planner.validator import PlannerValidator

class PlannerService:

    def __init__(
        self,
        adapter,
        registry,
    ):
        self.adapter = adapter
        self.registry = registry
        self.parser = PlannerParser()
        self.validator = PlannerValidator(registry)
    def plan(self, prompt):

        raw = self.adapter.generate(
            prompt,
            capabilities=self.registry.capabilities(),
        )

        print("=" * 50)
        print("PLANNER RAW")
        print(raw)
        print("=" * 50)

        raw_plan = self.parser.parse(raw)

        return self.validator.validate(raw_plan)