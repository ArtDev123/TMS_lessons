# Несколько потоков меняют один счёт без Lock — баланс расходится. Нужно защитить.
import threading
import time
from typing import Self


class BankAccount:
    def __init__(self, owner: str, balance: int) -> None:
        self.owner = owner
        self.balance = balance
        # RLock: тот же поток может взять блокировку повторно
        # (transfer вызывает withdraw/deposit, которые тоже берут lock).
        self._lock = threading.RLock()

    def withdraw(self, amount: int) -> bool:
        with self._lock:
            current = self.balance
            time.sleep(0.02)
            if current >= amount:
                self.balance = current - amount
                print(f"{self.owner}: снято {amount}. Остаток: {self.balance}")
                return True
            print(f"{self.owner}: недостаточно средств ({self.balance})")
            return False

    def deposit(self, amount: int) -> None:
        with self._lock:
            current = self.balance
            time.sleep(0.02)
            self.balance = current + amount
            print(f"{self.owner}: пополнено на {amount}. Остаток: {self.balance}")

    def transfer(self, other: Self, amount: int) -> bool:
        # Берём lock'и в одном порядке (по id), иначе deadlock:
        # поток A→B держит lock A и ждёт B, поток B→A — наоборот.
        first, second = (self, other) if id(self) < id(other) else (other, self)
        with first._lock:
            with second._lock:
                if not self.withdraw(amount):
                    return False
                other.deposit(amount)
                return True


print("=== Один счёт, снятие и пополнение ===")
account = BankAccount("Иван", 200)


def client_withdraw() -> None:
    for _ in range(8):
        account.withdraw(10)


def client_deposit() -> None:
    for _ in range(8):
        account.deposit(10)


threads = [
    threading.Thread(target=client_withdraw),
    threading.Thread(target=client_deposit),
    threading.Thread(target=client_withdraw),
    threading.Thread(target=client_deposit),
]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Итоговый баланс: {account.balance} (ожидали 200)")


print("\n=== Переводы между двумя счетами ===")
alice = BankAccount("Алиса", 100)
bob = BankAccount("Боб", 100)
start_total = alice.balance + bob.balance


def send_many(source: BankAccount, target: BankAccount, times: int) -> None:
    for _ in range(times):
        source.transfer(target, 10)


transfer_threads = [
    threading.Thread(target=send_many, args=(alice, bob, 5)),
    threading.Thread(target=send_many, args=(bob, alice, 5)),
    threading.Thread(target=send_many, args=(alice, bob, 5)),
    threading.Thread(target=send_many, args=(bob, alice, 5)),
]
for thread in transfer_threads:
    thread.start()
for thread in transfer_threads:
    thread.join()

end_total = alice.balance + bob.balance
print(f"Алиса: {alice.balance}, Боб: {bob.balance}")
print(f"Сумма: {end_total} (ожидали {start_total})")
