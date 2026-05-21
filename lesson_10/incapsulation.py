class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.__password = password  # "приватный" атрибут

    @property
    def password(self) -> str:
        return "********"  # Скрываем реальный пароль при чтении

    @password.setter
    def password(self, new_password: str) -> None:
        if len(new_password) < 6:
            print("Пароль слишком короткий!")
        else:
            self.__password = new_password


user = User("admin", "123456")
print(user.password)  # ********
user.password = "123"  # Пароль слишком короткий!
