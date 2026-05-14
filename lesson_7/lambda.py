add = lambda x, y: x + y
print(add(5, 3))  # Результат: 8

is_even = lambda x: x % 2 == 0
print(is_even(9))  # Результат: True


users: list[tuple] = [("Anna", 25), ("Ivan", 18), ("Oleg", 30)]

# # Сортируем по второму элементу кортежа (индекс 1)
users_sorted = sorted(users, key=lambda user: user[1])
print(users_sorted)
# Результат: [('Ivan', 18), ('Anna', 25), ('Oleg', 30)]
