from dataclasses import dataclass


@dataclass(kw_only=True)
class InventoryItem:
    name: str
    _quantity: int = 0

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        self._quantity = 0 if value < 0 else value

    @property
    def is_available(self) -> bool:
        return self.quantity > 0

    def __str__(self) -> str:
        status = "в наличии" if self.is_available else "нет в наличии"
        return f"{self.name}: {self.quantity} шт. ({status})"


item = InventoryItem(name="Яблоко", _quantity=10)
print(item)
print(item.is_available)

item.quantity = -5
print(item.quantity)
print(item.is_available)

# С kw_only=True позиционные аргументы запрещены:
# item2 = InventoryItem("Груша", 3)  # TypeError
