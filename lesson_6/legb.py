# G - Global: Видна во всем файле
x: str = "GLOBAL"


def outer_function() -> None:
    # E - Enclosing: Видна во вложенной функции
    # x = "ENCLOSING (внешняя функция)"

    def inner_function() -> None:
        # L - Local: Видна только здесь
        # x = "LOCAL"
        # print(locals())
        # print(globals())
        # global x
        # len = "aalsdkjf"

        print(f"Сейчас Python выбрал значение: {x}")

        # B - Built-in: Мы не создавали len, она встроена в Python
        print(f"Длина строки x: {len(x)}")

    inner_function()


outer_function()


# fuel_level = 100


# def fly_to_moon():
#     # global fuel_level

#     fuel_level = fuel_level - 50
#     print(f"Внутри: {fuel_level}")


# fly_to_moon()


# def create_counter():
#     count = 0  # Переменная в области Enclosing (не глобальная!)

#     def increment():
#         nonlocal count # Говорим: "ищи в функции выше"
#         count += 1
#         return count

#     return increment

# counter_one = create_counter()

# print(counter_one()) # Выведет 1
# print(counter_one()) # Выведет 2


some_dict: dict[int, str] = {
    1: "one",
    2: "two",
    3: 3,
}
