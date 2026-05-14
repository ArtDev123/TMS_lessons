data = ["100", "200", "сто", "400", "0"]


def safe_convert(value: str) -> int | None:
    try:
        return int(value)
    except ValueError:
        return None


if __name__ == "__main__":
    # Используем map для конвертации
    results = list(map(safe_convert, data))
    print(results)

# 1. Сейчас при ошибке возвращается None. Перепишите safe_convert так, чтобы при ValueError возвращалось 0.
# 2. Добавьте в цепочку map еще одну функцию, которая делит 1000 на каждое число из списка.
#    Обработайте возможный ZeroDivisionError внутри этой функции.
