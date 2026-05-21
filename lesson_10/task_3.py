from enum import Enum


class DietType(Enum):
    PREDATOR = "Хищник"
    HERBIVORE = "Травоядное"
    OMNIVORE = "Всеядное"


class Animal:
    def __init__(self, name: str, diet_type: DietType) -> None:
        self.name = name
        self.diet_type = diet_type

    def make_sound(self) -> None:
        pass  # Будет переопределено


class Lion(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, DietType.PREDATOR)

    def make_sound(self) -> None:
        print(f"{self.name} рычит: РРРР!")


class Monkey(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, DietType.OMNIVORE)

    def make_sound(self) -> None:
        print(f"{self.name} кричит: У-у-а-а!")


class Snake(Animal):
    def __init__(self, name: str) -> None:
        super().__init__(name, DietType.PREDATOR)

    def make_sound(self) -> None:
        print(f"{self.name} шипит: Сссс!")


class Zoo:
    def __init__(self) -> None:
        self.animals: list[Animal] = []

    def add_animal(self, animal: Animal) -> None:
        self.animals.append(animal)

    def roll_call(self) -> None:
        for animal in self.animals:
            animal.make_sound()

    def feed_predators(self) -> None:
        for animal in self.animals:
            if animal.diet_type == DietType.PREDATOR:
                print(f"Кормим хищника {animal.name}.")


zoo = Zoo()
zoo.add_animal(Lion("Симба"))
zoo.add_animal(Monkey("Обезьяна"))
zoo.add_animal(Snake("Змея"))
zoo.roll_call()
zoo.feed_predators()
