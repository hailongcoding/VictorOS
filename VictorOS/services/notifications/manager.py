from .notification import Notification


class NotificationManager:

    def __init__(self):
        self.notifications: list[Notification] = []

    def push(self, notification: Notification):
        self.notifications.append(notification)

    def all(self):
        return self.notifications

    def unread(self):
        return [
            n
            for n in self.notifications
            if not n.read
        ]

    def mark_read(self, notification: Notification):
        notification.read = True

    def clear(self):
        self.notifications.clear()