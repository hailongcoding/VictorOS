from JarvisOS.services.brain.tasks import BrainTask


DEFAULT_WORKERS = {
    BrainTask.CONVERSATION: "conversation",
    BrainTask.CODING: "coding",
    BrainTask.REASONING: "reasoning",
    BrainTask.RESEARCH: "research",
}