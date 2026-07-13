from openjarvis import Jarvis

j = Jarvis()

result = j.ask_full(
    """Do you currently have memory or do you know where your system files places ? Im having a hard time studying your infastructure
""",
    agent="orchestrator",
    tools=["code_interpreter", "file_read"]
)

print(result)

j.close()