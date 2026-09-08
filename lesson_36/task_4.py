# Собираем заказы последовательно. Дальше — продюсер и воркеры через Queue.
from multiprocessing import Process, Queue

ORDERS = [
    {"id": 1, "item": "ноутбук", "qty": 1},
    {"id": 2, "item": "мышь", "qty": 3},
    {"id": 3, "item": "клавиатура", "qty": 2},
    {"id": 4, "item": "монитор", "qty": 1},
    {"id": 5, "item": "наушники", "qty": 4},
]

WORKERS = 3


def process_order(order: dict) -> str:
    return f"заказ {order['id']}: {order['item']} x{order['qty']} собран"


def producer(orders: list[dict], tasks: Queue, worker_count: int) -> None:
    for order in orders:
        print(f"продюсер положил заказ {order['id']}")
        tasks.put(order)
    for _ in range(worker_count):
        tasks.put(None)


def worker(tasks: Queue, results: Queue) -> None:
    while True:
        order = tasks.get()
        if order is None:
            break
        result = process_order(order)
        print(result)
        results.put(result)


def run_sequential(orders: list[dict]) -> None:
    for order in orders:
        print(process_order(order))


if __name__ == "__main__":
    print("=== Последовательно ===")
    run_sequential(ORDERS)

    print("\n=== Queue: продюсер и воркеры ===")
    tasks: Queue = Queue()
    results: Queue = Queue()

    producer_process = Process(target=producer, args=(ORDERS, tasks, WORKERS))
    workers = [Process(target=worker, args=(tasks, results)) for _ in range(WORKERS)]
    producer_process.start()
    for process in workers:
        process.start()
    producer_process.join()
    for process in workers:
        process.join()

    collected = [res_queue.get() for _ in len(ORDERS)]
    print(f"результаты: {collected}")
