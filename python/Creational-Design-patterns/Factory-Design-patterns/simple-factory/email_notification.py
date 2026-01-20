from notification import Notification

class EmailNotification(Notification):
    def notify(self, message):
        print(f"email notification send for message -> {message}")
        
