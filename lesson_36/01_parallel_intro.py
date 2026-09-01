# Сравниваем последовательный запуск и несколько потоков:
# три «медленные» задачи подряд vs одновременно.
import threading
import time

from utils import timed


def slow_task(name: str, seconds: float) -> None:
    print(f"{name}: старт")
    x = 1000**2_000_000  # имитация ожидания (сеть, диск, таймер)
    print(f"{name}: готово за {seconds} сек.")


@timed("Последовательно")
def run_sequential() -> None:
    # Задачи идут одна за другой: 1 + 1 + 1 ≈ 3 сек.
    slow_task("A", 1)
    slow_task("B", 1)
    slow_task("C", 1)


@timed("Одновременно")
def run_concurrent() -> None:
    # Три потока ждут параллельно: должно быть ≈ 1 сек, не 3.
    threads = [
        threading.Thread(target=slow_task, args=("A", 1)),
        threading.Thread(target=slow_task, args=("B", 1)),
        threading.Thread(target=slow_task, args=("C", 1)),
    ]
    for thread in threads:
        thread.start()  # поток поехал, main не ждёт окончания
    for thread in threads:
        thread.join()  # ждём, пока все трое закончат


print("=== Последовательно ===")
run_sequential()

print("\n=== Несколько потоков ===")
run_concurrent()
