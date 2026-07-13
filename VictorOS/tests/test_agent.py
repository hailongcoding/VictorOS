from openjarvis import Jarvis

j = Jarvis()

result = j.ask_full(
    "What is 15% of 340?",
    agent="orchestrator",
    tools=["calculator"]
)

print(result)

j.close()