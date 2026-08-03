from abc import ABC, abstractmethod

from VictorOS.core.contracts.reasoning import Reasoning
from VictorOS.core.contracts.understanding import Understanding


class ReasoningAdapter(ABC):

    @abstractmethod
    def reason(
        self,
        understanding: Understanding,
    ) -> Reasoning:
        ...