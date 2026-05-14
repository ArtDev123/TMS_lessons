# from typing import Any


def calculate_area(width: int, heigh: int) -> int:
    """Вычисляет площадь прямоугольника."""

    res = width * heigh
    return res


# width и height — параметры
# 10 и 5 — аргументы
width = 5
heigh = 100

res = calculate_area(width=width, heigh=heigh)

# print(res)
some_dict: dict[int, str | int] = {
    1: "one",
    2: "two",
    3: 3,
}

for key, value in some_dict.items():
    print(key)
    print(value)


list_with_ints: list[list[int]] = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
]
