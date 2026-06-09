import sqlite3

from sqlite3 import Connection

conn: Connection = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER,
    rating REAL
)
""")

books = [
    ("Мастер и Маргарита", "Михаил Булгаков", 1967, 4.9),
    ("Преступление и наказание", "Фёдор Достоевский", 1866, 4.7),
    ("Дюна", "Фрэнк Герберт", 1965, 4.5),
    ("Понедельник начинается в субботу", "Братья Стругацкие", 1965, 4.8),
]
cursor.executemany(
    "INSERT INTO books (title, author, year, rating) VALUES (?, ?, ?, ?)", books
)
conn.commit()

# --- ДОБАВЛЕННЫЙ БЛОК: SELECT и PRINT ---

# 1. Пишем SQL-запрос для выборки всех книг с рейтингом выше 4.6
cursor.execute("SELECT title, author, rating FROM books WHERE rating > 4.6")

# 2. Достаем все результаты из курсора
all_books = cursor.fetchall()

# 3. Выводим красивый заголовок и перебираем строки в цикле
print("=== Список лучших книг (рейтинг > 4.6) ===")
for row in all_books:
    # row[0] - это title, row[1] - author, row[2] - rating
    print(f"Книга: {row[0]} | Автор: {row[1]} | Рейтинг: {row[2]}")
print("=========================================")

# ----------------------------------------

conn.close()
