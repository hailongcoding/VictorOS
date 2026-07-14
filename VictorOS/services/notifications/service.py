from VictorOS.core.base import BaseService

from .manager import NotificationManager
from .notification import Notification


class NotificationService(BaseService):

    def __init__(self):
        super().__init__("Notifications")

        self.manager = NotificationManager()

    def start(self):
        self.running = True
        print("[START] Notification Service")

    def stop(self):
        self.running = False
        print("[STOP] Notification Service")

    def notify(self, notification: Notification):
        self.manager.push(notification)