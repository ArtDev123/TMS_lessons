# Два потока открывают два файла в разном порядке — могут зависнуть.
from contextlib import contextmanager
from typing import Iterator
import threading
import time

file_a = threading.Lock()
file_b = threading.Lock()


@contextmanager
def acquire_both(
    first: threading.Lock, second: threading.Lock
) -> Iterator[None]:
    with first:
        print("открыл первый")
        time.sleep(0.1)
        with second:
            yield


def copy_ab() -> None:
    with acquire_both(file_a, file_b):
        print("copy_ab открыл A и B")


def copy_ba() -> None:
    with acquire_both(file_a, file_b):
        print("copy_ba открыл A и B")


threads = [
    threading.Thread(target=copy_ab),
    threading.Thread(target=copy_ba),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
