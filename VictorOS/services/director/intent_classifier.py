from VictorOS.services.brain.tasks import BrainTask


class IntentClassifier:
    """
    Determines what kind of task the user is requesting.
    """

    def classify(self, prompt: str) -> BrainTask:
        text = prompt.lower()

        if any(word in text for word in (
            "code",
            "python",
            "java",
            "c++",
            "debug",
            "function",
            "script",
        )):
            return BrainTask.CODING

        if any(word in text for word in (
            "research",
            "search",
            "find",
            "latest",
            "news",
        )):
            return BrainTask.RESEARCH

        if any(word in text for word in (
            "think",
            "reason",
            "solve",
            "logic",
            "math",
        )):
            return BrainTask.REASONING

        return BrainTask.CONVERSATION