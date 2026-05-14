# новый_список = [выражение for элемент in последовательность if условие]

# Задача: создать список квадратов нечетных чисел
# numbers = [1, 2, 3, 4, 5, 6]

# # Вариант 1: Через цикл for (Долго и многословно)
# # squares_loop = []

# # for n in numbers:
# #     if n % 2 == 1:
# #         squares_loop.append(n**2)

# # print(squares_loop)

# # Вариант 2: List Comprehension (Быстро и чисто)
# squares_comp = [n**2 for n in numbers if n % 2 == 1]

# print(squares_comp)  # [1, 9, 25]

# matrix = [[], [], []]

# # counter = 0

# for i in range(1, 4):
#     for j in range(1, 4):
#         matrix[i - 1].append(i * j)

# # print(counter)
# print(matrix)
# pass


# # # Создаем таблицу умножения (матрица 3x3)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
# pass

# # Результат в дебаггере будет выглядеть так:
# # [
# #  [1, 2, 3],
# #  [2, 4, 6],
# #  [3, 6, 9]
# # ]
