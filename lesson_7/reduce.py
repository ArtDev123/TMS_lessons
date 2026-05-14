from functools import reduce
from typing import Any


def multiply(x: int, y: int) -> int:
    return x * y


numbers: list[int] = [1, 2, 3, 4, 5]

# ( ( (1 * 2) * 3) * 4) * 5 = 120
total_product: int = reduce(lambda x, y: x * y, numbers)

# print(total_product)  # 120


# nums: list[int] = [47, 11, 42, 102, 13]

# # Сравниваем два числа и проносим большее дальше по цепочке
# maximum: int = reduce(lambda a, b: a if a > b else b, nums)

# print(maximum)  # 102


# cart: list[dict[str, Any]] = [
#     {"name": "Laptop", "price": 1200.0, "count": 1},
#     {"name": "Mouse", "price": 25.5, "count": 2},
#     {"name": "Monitor", "price": 300.0, "count": 1},
# ]

# # 0.0 — это начальное значение (инициализатор)
# # Оно попадает в 'current_total' на первом шаге
# final_bill: float = reduce(
#     lambda current_total, item: current_total + (item["price"] * item["count"]),
#     cart,
#     0.0,
# )

# print(f"Итого к оплате: {final_bill} $")  # 1551.0 $
