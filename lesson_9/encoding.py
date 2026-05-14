# # --- Пример 1: Кодирование и декодирование строк в памяти (str <-> bytes) ---
# original_text = "Привет, студенты!"

# # Кодируем строку в байты (encode).
# # Получаем нечитаемый для человека набор байтов.
# bytes_utf8 = original_text.encode("utf-8")
# bytes_windows = original_text.encode("cp1251")

# print("Оригинал:", original_text)
# print("Байты (UTF-8):", bytes_utf8)
# print("Байты (CP1251):", bytes_windows)

# # Декодируем обратно (decode)
# # Если попытаться декодировать байты cp1251 как utf-8, будет ошибка (UnicodeDecodeError)
# decoded_text = bytes_windows.decode("cp1251")
# print("Декодированный текст:", decoded_text)
# print("-" * 30)


# # --- Пример 2: Кодировки при чтении и записи файлов ---
file_name = "encoding_test.txt"

# # 1. Записываем файл в кодировке cp1251 (стандартная кириллица Windows)
with open(file_name, "w", encoding="cp1251") as f:
    f.write("Этот текст сохранен в Windows-1251")


# # 2. Демонстрация ошибки: пытаемся прочитать файл в неправильной кодировке
print("Попытка прочитать файл неправильно:")
try:
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
except UnicodeDecodeError as e:
    print(f"Поймали ошибку кодировки! {e}")

# # 3. Читаем файл в правильной кодировке
# print("Попытка прочитать файл правильно:")
# with open(file_name, "r", encoding="cp1251") as f:
#     correct_text = f.read()
#     print("Успех:", correct_text)
