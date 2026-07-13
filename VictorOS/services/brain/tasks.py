from enum import Enum


class BrainTask(str, Enum):
    CONVERSATION = "conversation"
    REASONING = "reasoning"
    CODING = "coding"
    RESEARCH = "research"