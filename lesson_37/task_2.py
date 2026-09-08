# Два кассира одновременно сажают человека на одно место.
import threading
import time

seats = {"12A": None, "12B": None, "12C": None}
lock = threading.Lock()


def book(passenger: str, seat: str) -> None:
    with lock:
        if seats[seat] is None:
            time.sleep(0.05)
            seats[seat] = passenger
            print(f"{passenger} занял {seat}")
        else:
            print(f"{seat} уже занято ({seats[seat]})")


def book_many(passenger: str, seats_list: list[str]) -> None:
    with lock:
        for seat in seats_list:
            if seats[seat] is None:
                time.sleep(0.05)
                seats[seat] = passenger
                print(f"{passenger} занял {seat}")
                return
        print(f"{passenger}: свободных мест нет")


threads = [
    threading.Thread(target=book, args=("Анна", "12A")),
    threading.Thread(target=book, args=("Иван", "12A")),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(f"итог: {seats}")

seats = {"12A": None, "12B": None, "12C": None}
wanted = ["12A", "12B"]
many_threads = [
    threading.Thread(target=book_many, args=("Оля", wanted)),
    threading.Thread(target=book_many, args=("Пётр", wanted)),
    threading.Thread(target=book_many, args=("Кира", wanted)),
]
for thread in many_threads:
    thread.start()
for thread in many_threads:
    thread.join()
print(f"итог book_many: {seats}")


# Сделай так, чтобы при занятом месте book возвращал False, а не только печатал.
# Запусти 5 пассажиров на 3 места и выведи, кто остался без билета.
