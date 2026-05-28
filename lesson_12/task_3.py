import math
from typing import Self


class Shape:
    def area(self) -> float:
        pass


class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> int:
        return self.side**2

    def __lt__(self, other: Self) -> bool:
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented


class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


def print_total_area(shapes: list[Shape]) -> None:
    total = sum(shape.area() for shape in shapes)
    print(f"Суммарная площадь: {total}")


sq1 = Square(2)
sq2 = Square(3)
print(sq1 < sq2)
print(sq1 > sq2)

shapes: list[Shape] = [Square(4), Circle(2)]
print_total_area(shapes)
