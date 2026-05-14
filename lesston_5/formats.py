from math import pi

name = "Алексей"
age = 25

# Ставим f перед строкой и используем {}
greeting = f"Привет, меня зовут {name}, и мне {age} лет., pi: {pi:.2f}"
print(greeting)
# Вывод: Привет, меня зовут Алексей, и мне 25 лет.

apples = 5
oranges = 3

print(f"У меня всего {apples + oranges} фруктов.")


pi = 3.1415926535
print(f"Число Пи: {pi:.2f}")

#
#


# city = "Москва"
# temperature = 20


# weater_report_template = "Сегодня в городе {} температура {} градусов."
# # Значения подставятся в {} по порядку
# weather_report = weater_report_template.format(city, temperature)
# print(weather_report)
# Вывод: Сегодня в городе Москва температура 20 градусов.

# 0 - это "чай", 1 - это "кофе"
# order = (
#     "Я люблю {0}, но по утрам обычно пью {1}. Да, {1} бодрит лучше, чем {0}!".format(
#         "чай", "кофе"
#     )
# )
# print(order)


message = "Моя любимая игра - {game}, а любимый фильм - {movie}.".format(
    game="Ведьмак", movie="Матрица"
)
print(message)
