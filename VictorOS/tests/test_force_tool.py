from openjarvis import Jarvis

j = Jarvis()

result = j.ask_full(
    "Use the calculator tool to compute 987654 * 123456. Do not do mental math.",
    agent="orchestrator",
    tools=["calculator"],
)

print(result)

j.close()