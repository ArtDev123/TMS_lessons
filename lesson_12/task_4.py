import re

CARD_NUMBER_PATTERN = re.compile(r"^\d{16}$|^\d{4}(-\d{4}){1,3}$")


class PaymentError(Exception):
    pass


class InvalidAmountError(PaymentError):
    pass


class PaymentFailedError(PaymentError):
    pass


class PaymentMethod:
    def pay(self, amount: int) -> None:
        raise NotImplementedError


class CardPayment(PaymentMethod):
    def __init__(self, card_number: str, balance: int) -> None:
        if not CARD_NUMBER_PATTERN.fullmatch(card_number):
            raise PaymentError(f"Некорректный номер карты: {card_number}")
        self.card_number = card_number
        self.balance = balance

    def pay(self, amount: int) -> None:
        if self.balance < amount:
            raise PaymentFailedError(
                f"Недостаточно средств на карте {self.card_number}. "
                f"Доступно: {self.balance}, требуется: {amount}"
            )
        self.balance -= amount
        print(f"Оплата картой {self.card_number}: списано {amount} руб.")


class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address: str, balance: int) -> None:
        self.wallet_address = wallet_address
        self.balance = balance

    def pay(self, amount: int) -> None:
        if self.balance < amount:
            raise PaymentFailedError(
                f"Недостаточно средств в кошельке {self.wallet_address}. "
                f"Доступно: {self.balance}, требуется: {amount}"
            )
        self.balance -= amount
        print(f"Оплата с кошелька {self.wallet_address}: списано {amount} руб.")


class Order:
    def __init__(self, item_name: str, price: int, quantity: int) -> None:
        if price < 0 or quantity < 0:
            raise InvalidAmountError("Цена и количество не могут быть отрицательными.")
        self.item_name = item_name
        self.price = price
        self.quantity = quantity

    @property
    def total_cost(self) -> int:
        return self.price * self.quantity

    def process_payment(self, payment_method: PaymentMethod) -> None:
        try:
            payment_method.pay(self.total_cost)
            print(f"Заказ «{self.item_name}» оплачен на сумму {self.total_cost} руб.")
        except PaymentFailedError as e:
            print(f"Ошибка оплаты: {e}")


order = Order("Ноутбук", 50000, 1)
card = CardPayment("1234-5678", 100000)
order.process_payment(card)

poor_card = CardPayment("0000-0000", 1000)
order.process_payment(poor_card)

try:
    Order("Телефон", -100, 1)
except InvalidAmountError as e:
    print(f"Ошибка заказа: {e}")

try:
    CardPayment("12-34", 1000)
except PaymentError as e:
    print(f"Ошибка карты: {e}")
