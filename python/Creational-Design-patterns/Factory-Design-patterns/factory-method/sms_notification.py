from notification import Noitification


class SmsNotification(Noitification):
    def notify(self, message):
        print(f"sms notify for the message {message}")
