from VictorOS.core.contracts.reasoning import (
    Decision,
    Reasoning,
)

from VictorOS.core.contracts.understanding import Understanding

from VictorOS.services.reasoning.adapter import ReasoningAdapter


class DummyReasoningAdapter(ReasoningAdapter):

    def reason(
        self,
        understanding: Understanding,
    ) -> Reasoning:

        return Reasoning(
            understanding=understanding,
            decisions=[
                Decision(
                    goal=understanding.goal,
                    capability="conversation",
                    confidence=1.0,
                    reason="Dummy reasoning adapter.",
                )
            ],
        )