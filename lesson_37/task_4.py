# Потребитель крутит пустой список вхолостую. Замени это на Condition.
import threading
import time

orders: list[str] = []


def producer() -> None:
    for i in range(4):
        time.sleep(0.2)
        orders.append(f"заказ-{i}")
        print(f"положили заказ-{i}")


def consumer() -> None:
    taken = 0
    while taken < 4:
        if orders:
            order = orders.pop(0)
            print(f"собрали {order}")
            taken += 1
        else:
            print("ожидание заказа")
            time.sleep(0.05)


threads = [
    threading.Thread(target=producer),
    threading.Thread(target=consumer),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()


# Заведи threading.Condition и общий список. Продюсер после append делает
# notify(), потребитель в цикле while not orders: condition.wait().

# Запусти двух потребителей. Продюсер должен notify_all() (или notify
# столько раз, сколько нужно), чтобы заказы не застряли у одного.

# Ограничь очередь: если в orders уже 2 элемента, продюсер сам делает wait(),
# пока потребитель не заберёт заказ (ограниченный буфер).
