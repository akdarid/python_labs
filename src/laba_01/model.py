class Notification:
    def __init__(self, message: str):
        self.message = message


class EmailNotification(Notification):
    def __init__(self, message: str, email: str):
        super().__init__(message)
        self.email = email


class SMSNotification(Notification):
    def __init__(self, message: str, phone: str):
        super().__init__(message)
        self.phone = phone


# АНТИПАТТЕРН — нужно переписать:
def process(notification):
    if type(notification) == EmailNotification:
        print(f"Email на {notification.email}: {notification.message}")
    elif type(notification) == SMSNotification:
        print(f"SMS на {notification.phone}: {notification.message}")


# После переработки должно работать так:
items = [EmailNotification("Привет", "a@b.com"),
         SMSNotification("Пока", "+79001234567")]
for item in items:
    item.process()  # каждый класс сам знает, что делать