
# Import the NotificationFactory class from notification-factory.py
from simple_factory import NotificationFactory

if __name__ == "__main__":
	# Example usage
	try:
		notification = NotificationFactory.create_factory("sms")
		notification.notify("Hello World")
	except ValueError as e:
		print(e)