# class Dog:
#     dog_count: int = 0

#     def __init__(self, name: str, age: int | None = 0) -> None:

#         self.name = name  # атрибут объекта
#         self.age = age  # атрибут объекта
#         Dog.dog_count += 1

#     def __del__(self) -> None:
#         print(f"Dog {self.name} was deleted!")

#     def bark(self) -> None:  # метод
#         print(f"{self.name}, age: {self.age} говорит: Гав!")


# # Создание объектов
# dog1 = Dog(
#     name="Рекс",
#     # age=None,
#     # age=3,
# )

# print(dog1.dog_count)

# dog2 = Dog("Шарик", 5)

# dog1.bark()

# del dog1

# dog2.bark()


# print(dog2.dog_count)


class SomeClass:
    def __init__(self, value: int) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


obj_1 = SomeClass(10)

str_obj_1: str = str(obj_1)

print(str_obj_1)
