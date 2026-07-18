class MessageBus:

    def __init__(self):
        self.subscribers = {}

    def subscribe(self, receiver, callback):
        self.subscribers[receiver] = callback

    def publish(self, message):

        callback = self.subscribers.get(
            message.receiver
        )

        if callback:
            callback(message)