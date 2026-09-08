# Синхронизация: Condition (жди, пока появится задача) и Semaphore (не больше N сразу).
import threading
import time

tasks: list[str] = []
has_task = threading.Condition()


# def producer() -> None:
#     for i in range(3):
#         time.sleep(2)
#         with has_task:
#             tasks.append(f"задача-{i}")
#             print(f"продюсер положил задача-{i}")
#             has_task.notify()  # будим одного спящего потребителя


# def consumer() -> None:
#     for _ in range(3):
#         with has_task:
#             while not tasks:
#                 has_task.wait()  # отпускает lock и спит, не крутит цикл вхолостую
#             task = tasks.pop(0)
#         print(f"потребитель взял {task}")


# print("=== Condition: wait / notify ===")
# workers = [
#     threading.Thread(target=producer),
#     threading.Thread(target=consumer),
# ]
# for thread in workers:
#     thread.start()
# for thread in workers:
#     thread.join()


semaphore = threading.Semaphore(2)


def download(name: str) -> None:
    print(f"{name}: в очереди")
    with semaphore:
        # Одновременно здесь не больше двух потоков.
        print(f"{name}: качаю")
        time.sleep(3)
        print(f"{name}: готово")


print("\n=== Semaphore(2): три загрузки, два слота ===")
# Третий должен подождать, пока один из первых двоих освободит слот.
downloads = [threading.Thread(target=download, args=(f"файл-{i}",)) for i in range(10)]

for thread in downloads:
    thread.start()
for thread in downloads:
    thread.join()
