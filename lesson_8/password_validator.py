class WeakPasswordError(Exception):
    """Собственное исключение для слабых паролей"""

    pass


def check_password(password: str) -> None:
    try:
        if len(password) < 8:
            raise WeakPasswordError("Пароль слишком короткий!")
        print("Пароль принят")
    except WeakPasswordError as e:
        print(f"Ошибка безопасности: {e}")


# 1. Добавьте проверку: если в пароле нет цифр, выбрасывайте WeakPasswordError с соответствующим текстом.
# 2. Оберните вызов функции в цикл while, пока не будет введен валидный пароль.


if __name__ == "__main__":

    check_password("123")
