import random
from typing import Any


def fetch_server_data() -> dict[str, Any]:
    # Имитируем разные ошибки сервера
    res = random.choice(["ok", "timeout", "auth_error", "no_data"])
    if res == "timeout":
        raise ConnectionError("Сервер не отвечает")
    if res == "auth_error":
        raise PermissionError("Неверный токен")
    if res == "no_data":
        raise ValueError("Пустой ответ")
    return {"status": 200, "data": [1, 2, 3]}


def main():
    try:
        result = fetch_server_data()
        print(f"Данные получены: {result}")
    except (ConnectionError, PermissionError) as e:
        print(f"Критическая ошибка сети: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {type(e).__name__}")


if __name__ == "__main__":
    main()
# 1. Добавьте специфический блок 'except ValueError', чтобы обрабатывать ситуацию 'no_data' отдельно.
# 2. Используйте блок 'finally', чтобы выводить сообщение "Сессия завершена" в любом случае.
# 3. Реализуйте 'raise' внутри блока 'except PermissionError', чтобы пробросить ошибку выше после логирования.
