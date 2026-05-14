from typing import Callable, Any


def simple_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        # Действия до запуска изначальной функции
        print(f"--- Запуск функции: {func.__name__} ---")

        # Запускаем изначальную функцию
        result = func(*args, **kwargs)

        # Действия после завершения изначальной функции
        print(f"--- Завершение функции: {func.__name__} ---")
        return result

    return wrapper
