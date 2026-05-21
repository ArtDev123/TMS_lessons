from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.is_on = False

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    def __del__(self) -> None:
        print(f"Устройство {self.brand} утилизировано")


class Laptop(Device):
    def turn_on(self) -> None:
        self.is_on = True
        print(f"Ноутбук {self.brand} загружает ОС...")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"Ноутбук {self.brand} завершает работу...")


class Smartphone(Device):
    def turn_on(self) -> None:
        self.is_on = True
        print(f"Смартфон {self.brand} разблокирован.")

    def turn_off(self) -> None:
        self.is_on = False
        print(f"Смартфон {self.brand} заблокирован.")


mac = Laptop("Apple")
mac.turn_on()
mac.turn_off()

phone = Smartphone("Samsung")
phone.turn_on()
phone.turn_off()

del mac
