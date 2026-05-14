from typing import Callable


def execute_operation(
    a: float | int,
    b: float | int,
    func: Callable[[float | int, float | int], float | int],
) -> float | int:
    """
    Принимает два числа и функцию, реализующую операцию.
    Это 'чистая' функция высшего порядка.
    """
    return func(a, b)


operations: dict[str, Callable[[float | int, float | int], float | int]] = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x**y,
    "%": lambda x, y: x % y,
}


def main() -> tuple[int | float,]:
    x, y = 11, 2

    print(f"Исходные числа: {x} и {y}\n" + "-" * 20)

    for symbol, func in operations.items():
        result = execute_operation(x, y, func)
        print(f"Операция [{symbol}]: {result}")


if __name__ == "main":
    main()


# Задание 4: Кастомное исключение и raise
# Проблема: Операция возведения в степень (^) может "повесить" компьютер, если передать слишком большие числа.
# Задача:
# 1. Создай свой класс исключения TooPowerfulError.
# 2. В блоке main или внутри execute_operation добавь проверку: если выполняется операция ^ и число y > 1000,
# инициируй свою ошибку через raise.
# 3. Обработай это исключение в цикле, чтобы программа просто пропускала эту операцию и шла дальше.

# Цель: Научиться создавать и вызывать собственные исключения.

# Задание 5: Отказоустойчивый калькулятор (else / finally)
# Задача: Доработай цикл в main так, чтобы:

# В блоке else выводилось сообщение: "Операция выполнена успешно".

# В блоке finally выводилось сообщение: "Завершение вычисления для [символ_операции]".

# Попробуй намеренно вызвать ошибку (например, KeyError, обратившись к несуществующей операции) и посмотри, как сработает finally.

# Цель: Закрепить понимание полной структуры блока обработки ошибок и логики работы else/finally.
