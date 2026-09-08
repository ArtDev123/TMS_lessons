# Считаем простые числа последовательно. Сравнить с потоками (GIL) и процессами.
import math
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from utils import timed

START = 1
END = 700_000

PARTS = 4


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, int(math.sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def count_primes(range_start: int, range_end: int) -> int:
    return sum(1 for number in range(range_start, range_end) if is_prime(number))


def count_primes_chunk(bounds: tuple[int, int]) -> int:
    return count_primes(*bounds)


def primes_in_range(bounds: tuple[int, int]) -> list[int]:
    range_start, range_end = bounds
    return [number for number in range(range_start, range_end) if is_prime(number)]


def make_chunks(start: int, end: int, parts: int) -> list[tuple[int, int]]:
    span = end - start
    size = span // parts
    chunks = []
    for i in range(parts):
        chunk_start = start + i * size
        chunk_end = end if i == parts - 1 else start + (i + 1) * size
        chunks.append((chunk_start, chunk_end))
    return chunks


@timed("Последовательно")
def run_sequential() -> int:
    return count_primes(START, END)


@timed("Потоки (GIL)")
def run_threads(chunks: list[tuple[int, int]]) -> int:
    with ThreadPoolExecutor(max_workers=PARTS) as pool:
        return sum(pool.map(count_primes_chunk, chunks))


@timed("Процессы")
def run_processes(chunks: list[tuple[int, int]]) -> int:
    with ProcessPoolExecutor(max_workers=PARTS) as pool:
        return sum(pool.map(count_primes_chunk, chunks))


@timed("Процессы, список простых")
def collect_primes(chunks: list[tuple[int, int]]) -> list[int]:
    with ProcessPoolExecutor(max_workers=PARTS) as pool:
        parts = list(pool.map(primes_in_range, chunks))
    primes: list[int] = []
    for part in parts:
        primes.extend(part)
    primes.sort()
    return primes


if __name__ == "__main__":
    chunks = make_chunks(START, END, PARTS)

    # sequential_total = run_sequential()
    # threads_total = run_threads(chunks)
    processes_total = run_processes(chunks)
    # print(
    #     f"Простых чисел: последовательно {sequential_total}, "
    #     f"потоки {threads_total}, процессы {processes_total}"
    # )

    # primes = collect_primes(chunks)
    # print(
    #     f"Собрали {len(primes)} простых, первые: {primes[:5]}, последние: {primes[-5:]}"
    # )
