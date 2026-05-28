class User:
    def __init__(self, username: str, role: str) -> None:
        self.username = username
        self.role = role

    @staticmethod
    def is_valid_username(username: str) -> bool:
        return len(username) >= 3


# Добавь метод класса create_admin(cls, username),
# который создает пользователя с ролью "admin".

# Добавь метод класса from_dict(cls, data),
# который принимает словарь вида {"username": "Ivan", "role": "user"}
# и возвращает готовый объект User.

# Модифицируй __init__,
# чтобы при создании пользователя проверялось имя с помощью is_valid_username.
# Если имя некорректно, выводи предупреждение (или бросай стандартную ошибку).
