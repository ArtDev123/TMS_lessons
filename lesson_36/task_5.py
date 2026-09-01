# Процесс считает сумму списка и возвращает её родителю через Pipe.
from multiprocessing import Pipe, Process


def worker(conn) -> None:
    numbers = conn.recv()
    total = sum(numbers)
    conn.send(total)
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    process = Process(target=worker, args=(child_conn,))
    process.start()

    parent_conn.send([10, 20, 30, 40])
    print(f"Сумма от процесса: {parent_conn.recv()}")
    process.join()


# Сделай канал двусторонним осмысленно: воркер не только считает сумму,
# но и отправляет назад отдельно чётные и нечётные числа.
# Родитель печатает оба списка.

# Добавь второй процесс: первый фильтрует отрицательные числа,
# второй считает статистику (min, max, avg) и возвращает словарь.
# Соедини их через Pipe (конвейер процессов).

# Замени один из Pipe на multiprocessing.Manager().dict()
# или Manager().list(): дочерний процесс пишет туда результат,
# а родитель читает после join(). Сравни, чем это удобнее/хуже очереди.
