# Шесть «запросов» идут сразу. Нужно пускать не больше трёх одновременно.
import threading
import time

from utils import timed


class Scrapper:
    semaphore = threading.Semaphore(3)

    def __init__(self, requests_count: int):
        self.requests_count = requests_count

    def fetch(self, name: str = ""):
        with self.semaphore:
            print(f"{name}: старт")
            time.sleep(5)
            print(f"{name}: ответ")

    def fetch_concurrent(self, name: str = ""):
        threads = [
            threading.Thread(target=self.fetch, args=(f"{name}-req-{i}",))
            for i in range(self.requests_count)
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()


def run_all() -> None:
    scrapper = Scrapper(requests_count=100)
    scrapper.fetch_concurrent("test")


run_all()


# Добавь печать «жду слот» до acquire и «взял слот» сразу после,
# чтобы было видно очередь.

# Сделай параметр max_inflight у run_all и прогони с 1, 3 и 6.
# Сравни три замера через @timed.
