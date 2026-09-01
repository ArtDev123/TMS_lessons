# Передаём данные между процессами: очередь задач (Queue) и ping/pong через Pipe.
from multiprocessing import Pipe, Process, Queue


def ping(conn) -> None:
    # Один конец Pipe — у ребёнка. recv/send — как разговор по трубке.
    message = conn.recv()
    conn.send(f"pong: {message}")
    conn.close()


if __name__ == "__main__":
    print("\n=== Pipe ===")
    # Два конца одного канала. Обычно один отдаём дочернему процессу.
    parent_conn, child_conn = Pipe()
    process = Process(target=ping, args=(child_conn,))
    process.start()
    parent_conn.send("ping")
    print(f"Родитель получил: {parent_conn.recv()}")  # pong: ping
    process.join()
