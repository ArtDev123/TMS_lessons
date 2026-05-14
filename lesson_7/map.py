from typing import Any

# def clean_and_int(item: str) -> int:
#     """Очищает строку от пробелов и конвертирует в число."""
#     return int(item.strip())


# raw_data: list[str] = ["  10", "20  ", " 30 "]

# # map возвращает итератор, поэтому оборачиваем в list для вывода
# converted: list[int] = list(map(lambda x: int(x.strip()), raw_data))

# print(converted)  # [10, 20, 30]


# def get_upper_name(person: dict[str, Any]) -> str:
#     return str(person["name"]).upper()


# users: list[dict[str, Any]] = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 35},
# ]

# # Применяем функцию к каждому словарю в списке
# names_list: list[str] = list(map(lambda x: (str(x["name"].upper()), x["age"]), users))

# print(names_list)  # ['ALICE', 'BOB', 'CHARLIE']


def format_price(product: str, price: float) -> str:
    return f"Товар: {product}, Цена: {price:.2f} руб."


products: list[str] = ["Кофе", "Чай", "Пирог"]
prices: list[float] = [150.5, 80.0, 210.99]

# map берет по одному элементу из каждого списка и передает в format_price
catalog: list[str] = list(map(format_price, products, prices))

for item in catalog:
    print(item)
# # Результат:
# # Товар: Кофе, Цена: 150.50 руб.
# # Товар: Чай, Цена: 80.00 руб.
# # Товар: Пирог, Цена: 210.99 руб.
