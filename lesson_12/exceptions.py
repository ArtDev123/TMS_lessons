class InsufficientFundsError(Exception):
    """Исключение, вызываемое при нехватке денег на счете."""

    def __init__(self, balance: int, amount: int) -> None:
        self.balance = balance
        self.amount = amount
        super().__init__(f"Попытка снять {amount} руб. Доступно только {balance} руб.")


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Успешно снято {amount}. Остаток: {self.balance}")


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Успешно снято {amount}. Остаток: {self.balance}")


account = BankAccount(500)
account.withdraw(600)
