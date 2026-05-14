# # Запись данных в файл с явным указанием кодировки utf-8
text_to_save = "Привет, мир! Изучаем Python."

with open("hello.txt", "w", encoding="utf-8") as file:
    file.write(text_to_save)

# # Чтение данных из файла
with open("hello.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Содержимое файла:", content)
