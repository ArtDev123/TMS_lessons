import os
import sys
import tracemalloc
from typing import Generator


# 1. Подготовка: создадим относительно большой файл для теста (~10 000 000 строк)
def create_test_log(file_path: str) -> None:
    with open(file_path, "w", encoding="utf-8") as f:
        for i in range(10000000):
            if i % 1000 == 0:
                f.write(f"Line {i}: ERROR - Something went wrong!\n")
            else:
                f.write(f"Line {i}: INFO - All systems nominal.\n")


# 2. Неэффективный подход: загрузка всего файла в память
def read_logs_bad(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        # readlines() сразу загружает ВСЕ строки в список в RAM
        lines = f.readlines()
        result = []
        for line in lines:
            if "ERROR" in line:
                result.append(line.strip())
        return result


# 3. Эффективный подход: генератор (ленивые вычисления)
def read_logs_good(file_path: str) -> Generator:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                yield line.strip()
                pass


# # --- ДЕМОНСТРАЦИЯ И ЗАМЕРЫ ---
log_file = "demo_server.log"
create_test_log(log_file)

print("=" * 50)
print(f"Размер файла на диске: {os.path.getsize(log_file) / (1024*1024):.2f} MB")
print("=" * 50)

# # --- ТЕСТ 1: Классический список (Плохой вариант) ---
tracemalloc.start()  # Включаем замер памяти

errors_list = read_logs_bad(log_file)
# Нас интересует peak — максимальный объем RAM, до которого прыгнула программа
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

bad_memory = peak / (1024 * 1024)
print(f"[Обычный список] Пиковое потребление RAM: {bad_memory:.2f} MB")
print(
    f"Размер сохраненного объекта списка в Python: {sys.getsizeof(errors_list) / 1024:.2f} KB"
)


print("-" * 50)


# # --- ТЕСТ 2: Генератор (Хороший вариант) ---
tracemalloc.start()  # Сбрасываем и включаем замер заново

errors_gen = read_logs_good(log_file)
# Имитируем обработку данных из генератора
for error_line in errors_gen:
    pass  # Просто читаем их по очереди, не сохраняя в список

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

good_memory = peak / (1024 * 1024)
print(f"[Генератор]      Пиковое потребление RAM: {good_memory:.2f} MB")
# Сам объект генератора весит копейки, сколько бы данных в нем ни было
print(f"Размер самого объекта генератора в Python: {sys.getsizeof(errors_gen)} байт")

print("=" * 50)
print(
    f"Результат: Генератор эффективнее примерно в {int(bad_memory / (good_memory if good_memory > 0 else 1))} раз(а)!"
)

# Очистка за собой
if os.path.exists(log_file):
    os.remove(log_file)
