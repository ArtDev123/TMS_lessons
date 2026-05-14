from typing import Callable


def outer_function(lst: list[int]) -> Callable[[], int]:

    def inner_function(element: int) -> int:
        lst.append(element)
        return lst

    return inner_function


# Создаем конкретные счетчики
closure = outer_function([1, 2, 3])

print(closure(5))
print(closure(11))
print(closure(15))
print(closure(21))
print(closure(3))
