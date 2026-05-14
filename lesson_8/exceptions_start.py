# def safe_divide(a: float, b: float) -> float | str:
#     try:
#         result = a / b
#     except ZeroDivisionError as e:
#         print(e)
#         result = "Ошибка: на ноль делить нельзя!"
#     return result


# # print(safe_divide(10, 2))
# print(safe_divide(10, 0))
try:
    x = 10 / 0
except ZeroDivisionError as e:
    print(f"exception: {e}")
    raise e
else:
    print("success")
finally:
    print("end")

# def get_age() -> None:
#     age_str = input("Введите ваш возраст: ")
#     try:
#         age = int(age_str)
#         print(f"Ваш возраст: {age}")
#     except ValueError:
#         print("Ошибка: введите числовое значение!")


# get_age()


# prices = {"apple": 100, "banana": 50, "orange": 80}


# def get_price(item: str) -> None:
#     try:
#         print(f"Цена {item}: {prices[item]}")
#     except KeyError:
#         print(f"Товара '{item}' нет в прайс-листе.")


# get_price("apple")
# get_price("mango")


# def process_file_mock(filename: str) -> None:
#     try:
#         print(f"Открываем файл {filename}...")
#         # Представим, что здесь работа с файлом
#         if filename == "error.txt":
#             raise FileNotFoundError
#     except FileNotFoundError:
#         print("Файл не найден!")
#     else:
#         print("Данные успешно прочитаны.")
#     finally:
#         print("Очистка ресурсов: файл закрыт.")


# process_file_mock("data.txt")


# def calculate_discount(price: float, discount: float) -> None:
#     assert 0 <= discount <= 100, "Скидка должна быть от 0 до 100%"
#     return price * (1 - discount / 100)


# print(calculate_discount(1000, 20))
# # print(calculate_discount(1000, 150)) # Вызовет AssertionError
