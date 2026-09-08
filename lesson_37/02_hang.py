# Зависание: поток ждёт событие, которое никто не отправит.
import threading
import time


ready = threading.Event()


def waiter() -> None:
    print("жду сигнал ready...")
    # wait() без timeout блокирует навсегда, если set() не вызовут.
    got = ready.wait(timeout=1.5)
    if got:
        print("сигнал пришёл, продолжаю")
    else:
        print("timeout: main забыл ready.set() — поток завис бы без ограничения")


print("=== Забыли отправить сигнал ===")
thread = threading.Thread(target=waiter)
thread.start()
time.sleep(0.3)
print("данные уже готовы, но set() нет")
thread.join()


ready = threading.Event()
print("\n=== Сигнал отправлен ===")
thread = threading.Thread(target=waiter)
thread.start()
time.sleep(0.2)
ready.set()  # все, кто ждал, просыпаются
thread.join()
print("поток завершился")
