from factory import NotificationFactory
from sms_notification import SmsNotification


class SmsNotificationFactory(NotificationFactory):
    def create(self):
        return SmsNotification()