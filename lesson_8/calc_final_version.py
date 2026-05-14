from typing import Callable


# Задание 4: Создаем собственное исключение
class TooPowerfulError(Exception):
    """Исключение для слишком больших вычислений"""

    pass


def execute_operation(
    a: float | int,
    b: float | int,
    func: Callable[[float | int, float | int], float | int],
) -> float | int:
    # Задание 3: Проверка типов через assert
    assert isinstance(a, (int, float)) and isinstance(
        b, (int, float)
    ), "Аргументы должны быть числами!"

    # Задание 1: Защита от ZeroDivisionError
    try:
        return func(a, b)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


operations: dict[str, Callable[[float | int, float | int], float | int]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x**y,
    "%": lambda x, y: x % y,
}


def get_number(prompt: str) -> float:
    # Задание 2: Безопасный ввод в цикле
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Это не число! Попробуйте еще раз.")


def main():
    print("--- Прокачанный калькулятор ---")

    x = get_number("Введите первое число (x): ")
    y = get_number("Введите второе число (y): ")

    print(f"\nИсходные числа: {x} и {y}\n" + "-" * 20)

    for symbol, func in operations.items():
        try:
            # Задание 4: Инициируем свое исключение через raise
            if symbol == "^" and y > 1000:
                raise TooPowerfulError(f"Степень {y} слишком велика!")

            result = execute_operation(x, y, func)

        except TooPowerfulError as e:
            # Обработка нашего кастомного исключения
            print(f"Операция [{symbol}]: Пропущена. Причина: {e}")

        except Exception as e:
            # На случай непредвиденных ошибок
            print(f"Операция [{symbol}]: Произошла системная ошибка: {e}")

        else:
            # Задание 5: Блок else (выполнится, если не было ошибок)
            print(f"Операция [{symbol}]: {result} (Успешно)")

        finally:
            # Задание 5: Блок finally (выполнится всегда)
            print(f"   [Лог]: Завершено вычисление для '{symbol}'")


# Исправлено: корректная проверка точки входа
if __name__ == "__main__":
    main()
