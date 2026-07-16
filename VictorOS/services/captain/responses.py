import random

TASK_STARTED = [
    "Working on it.",
    "I'm on it.",
    "Consider it done.",
    "I'll take care of it.",
    "Starting now.",
]

TASK_COMPLETED = [
    "Done.",
    "Finished.",
    "Task completed.",
]

TASK_FAILED = [
    "Something went wrong.",
    "I couldn't finish that task.",
]

GREETINGS = [
    "Hello.",
    "Hi.",
    "Good to see you.",
]

def random_response(options):
    return random.choice(options)