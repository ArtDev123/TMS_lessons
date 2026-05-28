from typing import Generator

# 1. Генератор списка (List Comprehension) — сразу создает весь список в памяти
squares_list = [x**2 for x in range(5)]
print(squares_list)  # [0, 1, 4, 9, 16]

# 2. Generator Expression — ленивый аналог в круглых скобках
squares_gen_expr = (x**2 for x in range(5))
print(squares_gen_expr)  # <generator object ...>


# 3. Генераторная функция — использует yield, возвращает генератор
def squares_generator(n: int) -> Generator:
    for x in range(n):
        yield x**2


# Демонстрация «ленивости»:
gen = squares_generator(5)
print(next(gen))  # 0
print(next(gen))  # 1
