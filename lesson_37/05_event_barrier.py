# Синхронизация: Event (один сигнал всем) и Barrier (ждём, пока соберутся все).
import threading
import time

# start_signal = threading.Event()


# def runner(name: str) -> None:
#     print(f"{name}: на старте, жду выстрел")
#     start_signal.wait()  # спим, пока кто-то не вызовет set()
#     print(f"{name}: побежал")


# print("=== Event: один set будит всех ===")
# runners = [
#     threading.Thread(target=runner, args=("Аня",)),
#     threading.Thread(target=runner, args=("Боря",)),
#     threading.Thread(target=runner, args=("Вика",)),
# ]
# for thread in runners:
#     thread.start()

# time.sleep(0.3)

# print("выстрел")
# start_signal.set()

# for thread in runners:
#     thread.join()


barrier = threading.Barrier(3)


def teammate(name: str, prepare_for: float) -> None:
    time.sleep(prepare_for)
    print(f"{name}: готов, жду команду")
    barrier.wait()  # последний из трёх отпускает всех сразу
    print(f"{name}: пошли вместе")


print("\n=== Barrier: выходим только втроём ===")
# Готовятся 0.1 / 0.4 / 0.2 сек. Печать «пошли» должна начаться после самой долгой.
team = [
    threading.Thread(target=teammate, args=("первый", 1)),
    threading.Thread(target=teammate, args=("второй", 4)),
    threading.Thread(target=teammate, args=("третий", 2)),
]
for thread in team:
    thread.start()
for thread in team:
    thread.join()
