# GIL на CPU-задаче: потоки не ускоряют счёт, процессы — ускоряют.
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from utils import timed

N = 8_000_000
WORKERS = 4


def cpu_bound(n: int) -> int:
    # Чистый Python-цикл: нужен GIL, ядро почти всё время занято интерпретатором.
    total = 0
    for i in range(n):
        total += i * i
    return total


@timed("Последовательно")
def run_sequential() -> None:
    # Эталон: 4 прогона подряд. Запоминаем время — с ним сравниваем остальное.
    for _ in range(WORKERS):
        cpu_bound(N)


@timed("Потоки (GIL мешает CPU)")
def run_threads() -> None:
    # Несколько потоков, но GIL пускает к bytecode только один.
    # Время должно быть ≈ как у последовательного запуска (или чуть хуже).
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(cpu_bound, [N] * WORKERS))


@timed("Процессы (каждый со своим GIL)")
def run_processes() -> None:
    # Отдельный процесс = отдельный интерпретатор = свой GIL.
    # На нескольких ядрах должно быть заметно быстрее (примерно в 2–4 раза).
    with ProcessPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(cpu_bound, [N] * WORKERS))


if __name__ == "__main__":
    run_sequential()
    run_threads()
    run_processes()
