from openjarvis import Jarvis

j = Jarvis()

result = j.ask_full(
    "List the files in the current directory using the shell tool.",
    agent="orchestrator",
    tools=["shell"]
)

print(result)

j.close()