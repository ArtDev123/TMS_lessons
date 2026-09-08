# Условие состязательности: check-then-act без Lock — два потока видят «свободно».
import threading
import time

# registered: list[str] = []


# # def register(username: str) -> None:
# #     # 1) читаем список  2) решаем  3) пишем.
# #     # Между 1 и 3 другой поток успевает сделать то же самое.
# #     if username not in registered:
# #         time.sleep(0.05)
# #         registered.append(username)
# #         print(f"зарегистрирован: {username}, всего {len(registered)}")
# #     else:
# #         print(f"имя занято: {username}")


# # print("=== Гонка: два потока регистрируют одно имя ===")
# # # Ожидали одну запись «anna». Часто будет две — уникальность сломана.
# # threads = [
# #     threading.Thread(target=register, args=("anna",)),
# #     threading.Thread(target=register, args=("anna",)),
# # ]
# # for thread in threads:
# #     thread.start()
# # for thread in threads:
# #     thread.join()

# # print(f"итог: {registered}")


lock = threading.Lock()
registered = []


def register_safe(username: str) -> None:
    with lock:
        if username not in registered:
            time.sleep(0.05)
            registered.append(username)
            print(f"зарегистрирован: {username}, всего {len(registered)}")
        else:
            print(f"имя занято: {username}")


print("\n=== Проверка и запись под одним Lock ===")
# Должно быть ровно ['anna']: второй увидел имя уже занятым.
threads = [
    threading.Thread(target=register_safe, args=("anna",)),
    threading.Thread(target=register_safe, args=("anna",)),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"итог: {registered}")
