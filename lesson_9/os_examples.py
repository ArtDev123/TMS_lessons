import os

# Получаем текущую рабочую директорию (абсолютный путь)
current_dir = os.getcwd()
print("Текущая папка:", current_dir)


# # Смотрим, что внутри папки
# files = os.listdir(current_dir)
# print("Файлы и папки внутри:", files)

# # Безопасное создание пути к файлу (работает и на Windows, и на Mac/Linux)
# file_path = os.path.join(current_dir, "data", "report.txt")
# print("Сформированный путь:", file_path)

# folder_path = "hello"

# if not os.path.exists(folder_path):
#     os.mkdir("hello")

# print(
#     os.replace(
#         os.path.join("hello_1", "hello_2", "hello_123.py"),
#         os.path.join("hello_1", "hi.py"),
#     )
# )
