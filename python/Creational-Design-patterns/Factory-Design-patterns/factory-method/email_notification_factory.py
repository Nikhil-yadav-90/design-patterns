from factory import NotificationFactory
from email_notification import EmailNotification

class EmailNotificationFactory(NotificationFactory):
    def create(self):
        return EmailNotification()