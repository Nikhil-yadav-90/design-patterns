from email_notification import EmailNotification
from sms_notification import SmsNotification

class NotificationFactory:
    _creators={
        "email":EmailNotification(),
        "sms":SmsNotification()
    }
    @classmethod
    def create_factory(self, type):
        if type not in self._creators:
            raise ValueError("No Such type present")
        return self._creators[type]
