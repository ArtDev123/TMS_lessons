class TooPowerfulError(Exception):
    """Исключение для слишком больших вычислений"""

    pass


def pow(a: int, b: int) -> int:
    if b > 10_000:
        raise TooPowerfulError
    return a**b


a = int(input("Enter first num: "))
b = int(input("Enter second num: "))

# try:
res = pow(a, b)
print(res)
# except TooPowerfulError:
#     print("Second num > 10000")
