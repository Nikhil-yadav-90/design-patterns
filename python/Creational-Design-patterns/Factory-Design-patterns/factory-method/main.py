from email_notification_factory import EmailNotificationFactory
from sms_notification_factory import SmsNotificationFactory
if __name__ == "__main__":
    factory = EmailNotificationFactory()
    notification  = factory.create()
    notification.notify("hello world")


    factory = SmsNotificationFactory()
    notification = factory.create()

    notification.notify("kese h app log")