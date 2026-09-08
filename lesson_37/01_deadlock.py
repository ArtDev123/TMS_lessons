# Взаимная блокировка: два потока берут два lock'а в разном порядке и зависают.
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def left_first() -> None:
    with lock_a:
        print("левый взял A, ждёт B")
        time.sleep(0.1)
        with lock_b:
            print("левый взял оба")  # сюда не попадём


def right_first() -> None:
    with lock_b:
        print("правый взял B, ждёт A")
        time.sleep(0.1)
        with lock_a:
            print("правый взял оба")  # сюда не попадём


print("=== Deadlock ===")
stuck = [
    threading.Thread(target=left_first, daemon=True),
    threading.Thread(target=right_first, daemon=True),
]
for thread in stuck:
    thread.start()
for thread in stuck:
    thread.join()


# def take_ordered(name: str) -> None:
#     # Оба потока берут lock'и в одном порядке: A, потом B. Цикла ожидания нет.
#     with lock_a:
#         print(f"{name} взял A")
#         time.sleep(0.1)
#         with lock_b:
#             print(f"{name} взял оба — работа сделана")


# print("\n=== Тот же захват, один порядок ===")
# # lock'и после deadlock всё ещё заняты зависшими потоками — берём новые.
# lock_a = threading.Lock()
# lock_b = threading.Lock()
# ok = [
#     threading.Thread(target=take_ordered, args=("первый",)),
#     threading.Thread(target=take_ordered, args=("второй",)),
# ]
# for thread in ok:
#     thread.start()
# for thread in ok:
#     thread.join()
# print("оба потока завершились")
