from typing import Self


class Wallet:
    def __init__(self, balance: float) -> None:
        self.balance = balance

    # Перегрузка оператора + (сложение двух кошельков)
    def __add__(self, other: Self) -> Self:
        if isinstance(other, Wallet):
            return Wallet(self.balance + other.balance)
        return NotImplemented

    # Перегрузка оператора == (сравнение балансов)
    def __eq__(self, other: Self) -> bool:
        if isinstance(other, Wallet):
            return self.balance == other.balance
        return False

    def __repr__(self):
        return f"Wallet({self.balance})"


wallet_class = Wallet

wallet = wallet_class(balance=100)

pass

# w1 = Wallet(100)
# w2 = Wallet(100)
# w3 = w1 + w2
# print(w3)  # Wallet(350)
# print(w1 == w2)  # False
