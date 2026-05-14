import csv
from typing import Any

# Списки
# ==========================================
print("--- Чтение и запись через списки ---")

# Данные для записи (список списков)
# list_rows = [
#     ["Имя", "Возраст", "Город"],
#     ["Иван", 25, "Москва"],
#     ["Анна", 22, "Минск"],
# ]

# # Записываем в CSV
# with open("people_lists.csv", "w", encoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(list_rows)

# # Читаем из CSV
# with open("people_lists.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(f"Строка-список: {row}")


# Словари
# ==========================================
print("\n--- Чтение и запись через словари ---")

# Данные для записи (список словарей)
dict_rows: dict[str, Any] = [
    {"Имя": "Иван", "Возраст": 25, "Город": "Москва"},
    {"Имя": "Анна", "Возраст": 22, "Город": "Минск"},
]

# Для DictWriter нам нужно явно указать названия колонок (ключи словаря)
fieldnames = ["Имя", "Возраст", "Город"]

# Записываем словари в CSV
with open("people_dicts.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    # writeheader() автоматически берет список fieldnames и делает из него первую строку-заголовок
    writer.writeheader()

    # writerows сам разложит значения словарей по правильным колонкам
    writer.writerows(dict_rows)

# # Читаем из CSV в виде словарей
with open("people_dicts.csv", "r", encoding="utf-8") as f:
    # DictReader автоматически читает первую строку файла как ключи для словарей
    reader = csv.DictReader(f)
    for row in reader:
        # Теперь мы можем обращаться к данным по понятным именам колонок!
        name = row["Имя"]
        city = row["Город"]
        print(
            f"Строка-словарь: Пользователь {name} живет в городе {city}. Весь объект: {row}"
        )
