from VictorOS.contracts.assistant_request import AssistantRequest


class CommandProcessor:

    def __init__(self, director):
        self.director = director

    def process(self, prompt: str):

        command = prompt.strip().lower()

        if command == "tasks":
            return self._tasks()

        request = AssistantRequest(
            prompt=prompt,
            task=None,
        )

        return self.director.dispatch(request)
    
    def _tasks(self):

        manager = self.director.runtime.task_manager

        tasks = manager.all()

        if not tasks:
            return "No tasks."

        lines = []

        lines.append("=" * 30)
        lines.append("VictorOS Tasks")
        lines.append("=" * 30)

        for task in tasks:

            lines.append(
                f"#{task.id:<3} "
                f"{task.name:<15} "
                f"{task.status.value}"
            )

        return "\n".join(lines)