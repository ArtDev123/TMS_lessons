# Воркеры ждут Event «кэш прогрет». Сейчас сигнал не отправляют — зависание.
import threading
import time

cache: dict[str, int] = {}
cache_ready = threading.Event()


def warmup() -> None:
    time.sleep(0.3)
    cache["users"] = 42
    print("кэш собран")
    # сигнал воркерам забыли отправить


def worker(name: str) -> None:
    print(f"{name}: жду кэш")
    cache_ready.wait()
    print(f"{name}: читаю {cache}")


threads = [
    threading.Thread(target=warmup),
    threading.Thread(target=worker, args=("воркер-1",), daemon=True),
    threading.Thread(target=worker, args=("воркер-2",), daemon=True),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join(timeout=1)
    
print(f"ещё живы: {[thread.is_alive() for thread in threads]}")


# В конце warmup вызови cache_ready.set(). Оба воркера должны напечатать
# словарь и завершиться. join уже можно без timeout.

# Добавь cache_ready.wait(timeout=0.5) и обработку «кэш не готов»:
# если сигнал не пришёл, воркер печатает ошибку и выходит, а не висит.

# После успешного прогрева сбрось событие cache_ready.clear() и покажи,
# что новый воркер снова будет ждать следующего set().
