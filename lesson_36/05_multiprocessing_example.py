# Запускаем дочерний процесс и считаем квадраты через Pool в нескольких процессах.
import os
import time
import sys
from multiprocessing import Pool, Process, current_process

from utils import timed

sys.set_int_max_str_digits(maxdigits=10000000)


def liam(number: int) -> int:
    # Каждый воркер пула — отдельный процесс, pid будет разный.
    print(f"{current_process().name} pid={os.getpid()} считает {number}^10_000_000")
    return number**2_000_000


def show_pid(label: str) -> None:
    print(f"{label}: pid={os.getpid()}")


@timed("Pool")
def run_pool(numbers: list[int]) -> bool:
    # map раздаёт числа воркерам и собирает результаты в том же порядке.
    with Pool(processes=4) as pool:
        res = pool.map(liam, numbers)
        return True


@timed("seq")
def run_sequential(numbers: list[int]) -> bool:
    final_result = []
    for number in numbers:
        result = liam(number)
        final_result.append(result)
    return True


if __name__ == "__main__":
    # На Windows/spawn дочерний процесс заново импортирует модуль —
    # без этой защиты он снова создал бы процессы (бесконечный fork).

    results = run_pool([1000, 2000, 1000, 5000])
    print(f"Результаты: {results}")
