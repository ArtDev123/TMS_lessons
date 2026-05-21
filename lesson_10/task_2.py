from typing import Self


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: Self) -> Self:
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(5, 1)
print(v1 + v2)


# Перегрузи оператор вычитания __sub__, чтобы можно было вычесть один вектор из другого (v1 - v2).

# Перегрузи оператор сравнения на равенство __eq__, чтобы два вектора считались равными, если их координаты x и y совпадают.

# Перегрузи метод __abs__ (чтобы можно было вызвать abs(v1)), который будет возвращать длину вектора (формула: корень из x^2 + y^2).
