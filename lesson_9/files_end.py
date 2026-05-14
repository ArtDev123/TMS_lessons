import sys

file_name = "secret_data.txt"

try:
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
        print(text)
except FileNotFoundError:
    print("Файл не найден")
    sys.exit()

word_count = len(text.split())

with open("result.txt", "w", encoding="utf-8") as f:
    f.write(f"Количество слов: {word_count}")
