from typing import Any


class Bird:
    def speak(self) -> str:
        return "Чирик-чирик"


class Duck:
    def speak(self) -> str:
        return "Кря-кря"


def make_sound(animal: Any) -> None:
    print(animal.speak())


make_sound(Bird())  # Чирик-чирик
make_sound(Duck())  # Кря-кря
