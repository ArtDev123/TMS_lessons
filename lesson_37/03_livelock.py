# Livelock: потоки не стоят, но вечно уступают друг другу — дело не делается.
import threading
import time

# Аня и Боря встретились в коридоре. Оба вежливо отходят в одну сторону —
# и снова стоят друг перед другом. Работа (пройти) не делается.
sync = threading.Barrier(2)


def polite_step(name: str) -> None:
    for attempt in range(1, 9):
        sync.wait()  # оба делают шаг одновременно
        # Одинаковая логика у обоих: на нечётных — направо, на чётных — налево.
        # Зеркально уступают в одну сторону и снова блокируют проход.
        direction = "направо" if attempt % 2 == 1 else "налево"
        print(f"{name}: отхожу {direction} (попытка {attempt})")
        time.sleep(0.05)
    print(f"{name}: {attempt} раз уступил — пути нет (livelock)")


print("=== Вежливая встреча в коридоре ===")
threads = [
    threading.Thread(target=polite_step, args=("Аня",)),
    threading.Thread(target=polite_step, args=("Боря",)),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
# Ожидаем: 8 пар строк «отхожу …», потом оба «пути нет».
# В deadlock потоки спят на lock. Здесь они активны, но прогресса нет.
