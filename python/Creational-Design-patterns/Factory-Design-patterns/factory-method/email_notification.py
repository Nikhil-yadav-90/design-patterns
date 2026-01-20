from notification import Noitification


class EmailNotification(Noitification):
    def notify(self, message):
        print(f"email notify for the message {message}")