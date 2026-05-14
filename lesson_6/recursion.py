# Базовый случай (Base case): Условие, при котором функция останавливается.
# Без него функция будет вызывать себя вечно, пока не случится RecursionError (переполнение стека).

# Рекурсивный шаг: Вызов функции с измененными (обычно уменьшенными) данными,
# чтобы приблизиться к базовому случаю.


# def factorial(n: int) -> int:
#     # Базовый случай: факториал 0 или 1 равен 1
#     # if n <= 1:
#     #     return 1

#     # Рекурсивный шаг
#     res = factorial(n - 1)
#     return n * res


# print(factorial(7))  # 120

# F(7) = 7 * F(6) = 7 * 6 * F(5) = 7 * 6 * 5 * F(4) = 7 * 6 * 5 * 4 * F(3) =
# = 7 * 6 * 5 * 4 * 3 * F(2) = 7 * 6 * 5 * 4 * 3 * 2 * F(1) - базовый случай = 7 * 6 * 5 * 4 * 3 * 2 * 1 = ...


# def deep_sum(nested_list: list) -> int:
#     total = 0
#     for element in nested_list:
#         if isinstance(element, list):
#             # Если элемент — это список, ныряем в него (рекурсия)
#             total += deep_sum(element)
#         else:
#             # Если это число, просто прибавляем
#             total += element
#     return total


# data = [1, [2, [3, 4, [5, [1, [2, 3, 4, [4, [1, 4]]]]]], 5], 6, [1, 2, 3]]

# print(deep_sum(data))  # 27


# Числа Фибоначчи
# Это ряд чисел, где каждое последующее равно сумме двух предыдущих:
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Математическая модель идеальна для рекурсии: F(n) = F(n-1) + F(n-2)

# counter = 0


# def fibonacci(n: int) -> int:
#     global counter
#     counter += 1
#     # Базовый случай: первые два числа ряда
#     if n <= 0:
#         return 0
#     if n == 1:
#         return 1

#     # Рекурсивный шаг: вызываем функцию дважды!
#     return fibonacci(n - 1) + fibonacci(n - 2)


# print(fibonacci(36))


# # Кэш для хранения результатов: {номер_числа: значение}
# cache = {0: 0, 1: 1}


# def fib_fast(n: int) -> int:
#     global counter
#     counter += 1
#     if n in cache:
#         return cache[n]

#     # Сначала вычисляем, потом сохраняем в словарь
#     cache[n] = fib_fast(n - 1) + fib_fast(n - 2)
#     return cache[n]


# print(fib_fast(500))
# print(counter)

# O(2 * n) = O(n)

# mat_3_x_3 = [
#     [1, 2, 3],
#     [1, 2, 3],
#     [1, 2, 3],
# ]
