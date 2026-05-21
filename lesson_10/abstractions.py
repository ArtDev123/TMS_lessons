from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass


class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def area(self) -> int:
        return self.side**2


# shape = Shape() # Ошибка! Нельзя создать объект абстрактного класса
square = Square(5)
print(square.area())  # 25
