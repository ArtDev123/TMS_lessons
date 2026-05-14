# from lesson_7.simple_logger_decorator import simple_logger
from functools import wraps
from typing import Callable, Any

# def simple_logger(func: Callable[..., Any]) -> Callable[..., Any]:
#     def wrapper(*args: Any, **kwargs: Any) -> Any:

#         # Действия до запуска изначальной функции
#         print(f"--- Запуск функции: {func.__name__} ---")

#         # Запускаем изначальную функцию
#         result = func(*args, **kwargs)

#         # Действия после завершения изначальной функции
#         print(f"--- Завершение функции: {func.__name__} ---")
#         return result

#     return wrapper


# @simple_logger
# def say_hello(name: str) -> None:
#     print(f"Привет, {name}!")


# @simple_logger
# def add(x: int, y: int) -> int:
#     print(x + y)


# say_hello("Алексей")

# add(1, 2)


def check_admin(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(user_role: str, *args: Any, **kwargs: Any) -> Any:
        if user_role != "admin":
            print("Ошибка: Доступ запрещен! Нужны права админа.")
            return None
        return func(user_role, *args, **kwargs)

    return wrapper


@check_admin
def delete_database(user_role: str) -> None:
    print("База данных успешно удалена (шутка).")


delete_database("guest")  # Доступ запрещен
delete_database("admin")  # Выполнится


def repeat(times: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)  # Сохраняет имя и docstring оригинальной функции
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def send_alert(message: str) -> None:
    """Отправляет важное уведомление."""
    print(f"ALERT: {message}")


# # # Проверка метаданных
# print(f"Функция: {send_alert.__name__}")
print(f"Описание: {send_alert.__doc__}")

send_alert("System Overheat!")


@repeat(times=3)
def greet() -> None:
    print("Привет!")


greet()  # Напечатает "Привет!" три раза
