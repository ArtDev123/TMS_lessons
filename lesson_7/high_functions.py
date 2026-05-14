from typing import Callable


# rule: Callable[[str], bool] означает функцию,
# которая принимает строку и возвращает True/False


def check_data(
    items: list[str],
    rule: Callable[[str], bool],
) -> list[str]:
    result: list[str] = []
    for item in items:
        if rule(item):  # вызов фунции is_long
            result.append(f"{item} - OK")
        else:
            result.append(f"{item} - Error")
    return result


# # Примеры использования
is_long: Callable[[str], bool] = lambda x: len(x) > 5
data: list[str] = ["abc", "password123", "qwerty"]

print(check_data(data, is_long))


# def make_greeter(greeting: str) -> Callable[[str], str]:
#     """Возвращает функцию, которая приветствует человека."""

#     def greet(name: str) -> str:
#         return f"{greeting}, {name}!"

#     return greet


# # # hello_func — это теперь функция, принимающая str и возвращающая str
# # hello_func: Callable[[str], str] = make_greeter("Привет")
# hi_func: Callable[[str], str] = make_greeter("Hi!")

# print(hi_func("Алексей"))  # Привет, Алексей!


# def call_with_five(function: Callable[[int], int]) -> int:
#     return function(5)


# def add_one(number: int) -> int:
#     return number + 1


# def minus_one(number: int) -> int:
#     return number - 1


# result_add = call_with_five(add_one)

# result_minus = call_with_five(minus_one)

# print(result_add)
# print(result_minus)
