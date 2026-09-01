# Смотрим разницу процесса и потока: pid, id потока и общая/изолированная память.
import os
import threading
from multiprocessing import Process

shared_data = ["main"]


def show_identity(label: str) -> None:
    # Процесс = pid ОС. Поток = свой id, но pid тот же, что у родителя.
    print(
        f"{label}: pid={os.getpid()}, "
        f"thread={threading.get_ident()}, "
        f"data={shared_data}"
    )


def thread_worker() -> None:
    shared_data.append("thread")  # меняем список родителя: память общая
    show_identity("Поток")


def process_worker() -> None:
    shared_data.append("process")  # меняем СВОЮ копию списка
    show_identity("Процесс")


if __name__ == "__main__":
    show_identity("Главный процесс")

    thread = threading.Thread(target=thread_worker)
    thread.start()
    thread.join()
    # Должно быть ['main', 'thread']: поток писал в ту же память.
    print(f"После потока в main: {shared_data}")

    shared_data.clear()
    shared_data.append("main")

    process = Process(target=process_worker)
    process.start()
    process.join()
    # В процессе data=['main', 'process'], здесь снова ['main']:
    # у процесса своя память, изменения сюда не возвращаются.
    print(f"После процесса в main: {shared_data}")
