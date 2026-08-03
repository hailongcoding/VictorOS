from VictorOS.services.ai.client import AIClient
from VictorOS.services.intent.builder import (
    UnderstandingPromptBuilder,
)

from VictorOS.services.intent.repair import (
    UnderstandingRepairBuilder,
)

from VictorOS.services.intent.validator import (
    parse,
    validate,
)


class IntentService:
    def __init__(self):

        self.ai = AIClient()

        self.builder = UnderstandingPromptBuilder()

        self.repair_builder = UnderstandingRepairBuilder()

    def understand(self, text: str):

        # -------------------------------
        # First attempt
        # -------------------------------

        package = self.builder.build(text)

        raw = self.ai.chat(
            model="qwen3:0.6b",
            package=package,
            think=False,
        )

        try:

            understanding = parse(raw)

            issues = validate(understanding)

            if not issues:
                return understanding

        except Exception as e:

            issues = [str(e)]

        # -------------------------------
        # One repair attempt
        # -------------------------------

        repair_package = self.repair_builder.build(
            previous_output=raw,
            validation_errors=issues,
        )

        repaired_raw = self.ai.chat(
            model="qwen3:0.6b",
            package=repair_package,
            think=False,
        )
        
        understanding = parse(repaired_raw)

        issues = validate(understanding)

        if issues:

            raise ValueError(
                "Understanding failed after repair:\n"
                + "\n".join(issues)
            )

        return understanding