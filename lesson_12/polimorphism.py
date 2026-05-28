class Notification:
    def send(self, message: str) -> None:
        pass


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Отправка SMS: {message}")


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Отправка Email: {message}")


# Функция принимает любой объект, умеющий делать .send()
def notify_user(notifier: Notification, text: str) -> None:
    notifier.send(text)


# Демонстрация:
sms = SMSNotification()
email = EmailNotification()

notify_user(sms, "Привет! Твой код: 4422")
notify_user(email, "Вы успешно зарегистрировались!")
