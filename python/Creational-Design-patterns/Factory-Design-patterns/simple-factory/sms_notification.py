from notification import Notification


class SmsNotification(Notification):
    def notify(self, message):
        print(f"sms notification send for message -> {message}")