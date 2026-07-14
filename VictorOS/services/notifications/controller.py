from .service import NotificationService
from .notification import Notification


class NotificationController:

    def __init__(self, service: NotificationService):
        self.service = service

    def send(self, notification: Notification):
        self.service.notify(notification)

    def all(self):
        return self.service.all()

    def clear(self):
        self.service.clear()