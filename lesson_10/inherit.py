class Animal:
    def __init__(self, name: str) -> str:
        self.name = name

    def eat(self) -> None:
        print(f"{self.name} кушает.")


class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)  # Вызов __init__ родителя
        self.color = color

    def meow(self) -> None:
        print(f"{self.color} кот {self.name} мяукает.")


cat = Cat("Барсик", "Рыжий")
cat.eat()  # Метод родителя
cat.meow()  # Свой метод
