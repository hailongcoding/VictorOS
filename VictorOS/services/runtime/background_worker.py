from threading import Thread


class BackgroundWorker(Thread):
    """
    Executes a Runtime task in the background.

    This is intentionally lightweight.
    Future versions will support cancellation,
    progress reporting, priorities and scheduling.
    """

    def __init__(self, target, *args):
        super().__init__(daemon=True)
        self._target = target
        self._args = args

    def run(self):
        self._target(*self._args)