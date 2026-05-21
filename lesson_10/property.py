class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price  # При инициализации сразу вызывается сеттер

    # Геттер
    @property
    def price(self) -> str:
        print(f"Чтение цены для товара '{self.name}'")
        return self.__price

    # Сеттер
    @price.setter
    def price(self, value: int) -> None:
        print(f"Изменение цены для товара '{self.name}' на {value}")
        if value < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = value

    # Делитер
    @price.deleter
    def price(self) -> None:
        print(f"Удаление цены для товара '{self.name}'")
        del self.__price


# Демонстрация работы
laptop = Product("Ноутбук", 1500)

print(laptop.price)  # Отработает геттер
laptop.price = 1400  # Отработает сеттер

del laptop.price  # Отработает делитер

# print(laptop.price)   # Если раскомментировать, будет ошибка AttributeError, так как __price удален
