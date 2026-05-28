from typing import Any, Self


class RepeatingListIterator:
    def __init__(self, items: list, max_turns: int | None = None) -> None:
        self.items = items
        self.index = 0
        self.max_turns = max_turns
        self.count = 0

    def __next__(self) -> Any:
        if not self.items:
            raise StopIteration
        if self.count >= self.max_turns:
            raise StopIteration

        value = self.items[self.index]
        self.index = (self.index + 1) % len(self.items)
        self.count += 1
        return value


class RepeatingListIterable:
    def __init__(self, items: list, max_turns: int | None = None) -> None:
        self.items = items
        self.max_turns = max_turns

    def __iter__(self) -> RepeatingListIterator:
        return RepeatingListIterator(self.items, self.max_turns)


class RepeatingList:
    """Итерируемый объект и итератор в одном классе."""

    def __init__(self, items: list, max_turns: int | None = None) -> None:
        self.items = items
        self.max_turns = max_turns
        self.index = 0
        self.count = 0

    def __iter__(self) -> Self:
        self.index = 0
        self.count = 0
        return self

    def __next__(self) -> Any:
        if not self.items:
            raise StopIteration
        if self.max_turns is not None and self.count >= self.max_turns:
            raise StopIteration

        value = self.items[self.index]
        self.index = (self.index + 1) % len(self.items)
        self.count += 1
        return value


# Раздельные классы
data = RepeatingListIterable(["A", "B", "C"])
print(list(data))  # ['A', 'B', 'C', 'A', 'B', 'C', 'A']

# Объединённый класс
repeating = RepeatingList(["X", "Y"], max_turns=5)
print(list(repeating))  # ['X', 'Y', 'X', 'Y', 'X']
