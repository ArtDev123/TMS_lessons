class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.__balance = balance
        self.__history: list[str] = []

    def deposit(self, amount: int) -> None:
        self.__balance += amount
        self.__history.append(f"Пополнение на {amount}")
        print(f"Счет пополнен на {amount}.")

    def withdraw(self, amount: int) -> None:
        if amount > self.__balance:
            print("Недостаточно средств для снятия.")
            return
        self.__balance -= amount
        self.__history.append(f"Снятие {amount}")
        print(f"Со счета снято {amount}.")

    @property
    def balance(self) -> int:
        return self.__balance

    def show_history(self) -> None:
        for record in self.__history:
            print(record)


account = BankAccount("Иван", 100)
account.deposit(50)
print(account.balance)
account.withdraw(30)
account.withdraw(200)
account.show_history()
