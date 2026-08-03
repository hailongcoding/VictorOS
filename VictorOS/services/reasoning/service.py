from VictorOS.core.contracts.reasoning import Reasoning
from VictorOS.core.contracts.understanding import Understanding

from .adapter import ReasoningAdapter


class ReasoningService:

    def __init__(
        self,
        adapter: ReasoningAdapter,
    ):
        self.adapter = adapter

    def reason(
        self,
        understanding: Understanding,
    ) -> Reasoning:

        return self.adapter.reason(
            understanding
        )