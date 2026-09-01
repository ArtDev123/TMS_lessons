# Покупаем билеты из двух потоков: без Lock продаём лишнее, с Lock — нет.
import threading
import time

tickets_left = 5
lock = threading.Lock()


# def buy_without_lock(buyer: str, count: int) -> None:
#     global tickets_left
#     for _ in range(count):
#         # Гонка: читаем, засыпаем, пишем. Второй поток успевает прочитать
#         # то же число — оба «покупают» один билет, остаток врёт.
#         current = tickets_left
#         time.sleep(20)
#         if current > 0:
#             tickets_left = current - 1
#             print(f"{buyer} купил билет. Осталось: {tickets_left}")


def buy_with_lock(buyer: str, count: int) -> None:
    global tickets_left
    for _ in range(count):
        # with lock: пока один покупает, второй ждёт у входа.
        # Проверка и tickets_left -= 1 идут как одна операция.
        with lock:
            if tickets_left <= 0:
                print(f"{buyer}: билетов нет")
                return
            tickets_left -= 1
            print(f"{buyer} купил билет. Осталось: {tickets_left}")


def run_buyers(target) -> None:
    # 5 билетов, двое хотят по 4. Честно можно продать только 5.
    threads = [
        threading.Thread(target=target, args=("Анна", 4)),
        threading.Thread(target=target, args=("Иван", 4)),
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# print("=== Без блокировки (гонка данных) ===")
# run_buyers(buy_without_lock)
# # Часто останется не 0: продали больше 5 или счётчик «поплыл».
# print(f"Итого осталось: {tickets_left}")

# tickets_left = 5
print("\n=== С Lock ===")
run_buyers(buy_with_lock)
# Должно быть ровно 0: пятый билет ушёл, остальные услышали «билетов нет».
print(f"Итого осталось: {tickets_left}")
