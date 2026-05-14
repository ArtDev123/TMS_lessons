def get_bounded_input(prompt: str, low: int, high: int) -> int:
    while True:
        try:
            val = int(input(prompt))
            if not (low <= val <= high):
                raise ValueError(f"Число вне диапазона {low}-{high}")
            return val
        except ValueError as e:
            print(f"Неверный ввод: {e}. Попробуйте еще раз.")


if __name__ == "__main__":
    val = get_bounded_input("Enter number form 1 to 100", 1, 100)
    print(val)

# 1. Добавьте возможность выхода из цикла, если пользователь ввел
# слово "exit" (используйте raise для выхода).

# 2. Ограничьте количество попыток ввода до 3-х.
# Если попытки исчерпаны, выбросите собственное исключение OutOfAttemptsError.
