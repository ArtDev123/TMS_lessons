from typing import Any


# def is_positive(n: int) -> bool:
#     return n > 0


# numbers: list[int] = [-5, 3, -1, 10, 0, 7]

# # Очищаем список от отрицательных чисел и нулей
# result: list[int] = list(filter(lambda x: x > 0, numbers))

# print(result)  # [3, 10, 7]


# words: list[str] = ["apple", "it", "python", "hi", "code"]

# # Оставляем только слова, длина которых больше 3 символов
# long_words: list[str] = list(filter(lambda x: len(x) > 3, words))

# print(long_words)  # ['apple', 'python', 'code']


def is_eligible_sales_staff(user: dict[str, Any]) -> bool:
    """Проверяет соответствие сотрудника трем критериям."""
    is_active = user.get("is_active", False)
    in_sales = user.get("department") == "sales"
    is_adult = user.get("age", 0) >= 18

    return is_active and in_sales and is_adult


users: list[dict[str, Any]] = [
    {"name": "Ivan", "age": 25, "department": "sales", "is_active": True},
    {"name": "Maria", "age": 17, "department": "sales", "is_active": True},
    {"name": "Oleg", "age": 30, "department": "it", "is_active": True},
    {"name": "Anna", "age": 22, "department": "sales", "is_active": False},
    {"name": "Alex", "age": 40, "department": "sales", "is_active": True},
]

# Пропускаем через фильтр наш список пользователей
targeted_users: list[dict[str, Any]] = list(filter(is_eligible_sales_staff, users))

# Выведем только имена для наглядности
print([u["name"] for u in targeted_users])  # ['Ivan', 'Alex']


# # сделать Enum для department
