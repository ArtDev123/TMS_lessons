# Семейство алгоритмов (Стратегий)
class NormalBilling:
    def calculate(self, price: float) -> float:
        return price


class HappyHourBilling:
    def calculate(self, price: float) -> float:
        return price * 0.5


# Контекст, использующий стратегию
class Order:
    def __init__(
        self, price: float, billing_strategy: NormalBilling | HappyHourBilling
    ) -> NormalBilling:
        self.price = price
        self.strategy = billing_strategy

    def get_total(self) -> int:
        return self.strategy.calculate(self.price)


# Демонстрация:
order = Order(100, NormalBilling())
print(order.get_total())  # 100

# Меняем поведение на лету (полиморфизм в действии)
order.strategy = HappyHourBilling()
print(order.get_total())  # 50.0
