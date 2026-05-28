from typing import Self


class CountdownIterator:
    """Итератор: помнит ТЕКУЩЕЕ состояние и делает шаг."""

    def __init__(self, current: int) -> None:
        self.current = current

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration  # Сигнал об окончании цикла
        self.current -= 1
        return self.current + 1


class CountdownIterable:
    """Итерируемый объект: знает НАЧАЛО, но сам не бегает."""

    def __init__(self, start: int) -> None:
        self.start = start

    def __iter__(self) -> CountdownIterator:
        # Возвращает новый объект-итератор
        return CountdownIterator(self.start)


counter = CountdownIterable(3)

counter_iterator = counter.__iter__()

print(next(counter_iterator))

print(next(counter_iterator))

print(next(counter_iterator))

print(next(counter_iterator))
# for num in counter:
#     print(num)  # Выведет: 3, 2, 1
