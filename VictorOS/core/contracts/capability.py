from enum import Enum


class Capability(str, Enum):

    CONVERSATION = "conversation"

    CODING = "coding"

    RESEARCH = "research"

    VISION = "vision"

    AUTOMATION = "automation"