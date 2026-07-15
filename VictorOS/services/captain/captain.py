class Captain:

    def acknowledge(self, task):

        messages = {
            "conversation": "I'm here.",
            "coding": "Coding task created.",
            "research": "Research task created.",
        }

        return messages.get(
            task,
            "Working on it."
        )