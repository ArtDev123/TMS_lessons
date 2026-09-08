# Декоратор @timed: замер времени выполнения функции.
from functools import wraps
from time import perf_counter
from typing import Any, Callable


def timed(label: str | None = None) -> Callable:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = perf_counter()
            result = func(*args, **kwargs)
            elapsed = perf_counter() - start
            name = label if label is not None else func.__name__
            print(f"{name}: {elapsed:.2f} сек.")
            return result

        return wrapper

    return decorator
