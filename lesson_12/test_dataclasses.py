from dataclasses import dataclass


@dataclass
class Product:
    name: str
    _price: float  # инкапсуляция

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self._price = value


# Демонстрация:
if __name__ == "__main__":
    item = Product("Ноутбук", 50000)
    print(item)  # Автоматический __repr__: Product(name='Ноутбук', _price=50000)
    # item.price = 55000  # Работает сеттер
    print(item.price)
