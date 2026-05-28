import random
from typing import Generator


def random_numbers_generator(
    low: int, high: int, count: int | None = None
) -> Generator[int, None, None]:
    counter = 0
    while count is None or counter < count:
        yield random.randint(low, high)
        counter += 1


print(list(random_numbers_generator(1, 10, count=5)))

even_random = (n for n in random_numbers_generator(1, 100) if n % 2 == 0)

attempts = 0
while True:
    attempts += 1
    if next(even_random) == 50:
        break

print(f"Число 50 выпало на {attempts}-й попытке")
