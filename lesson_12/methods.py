from typing import Self


class DateConverter:
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    # Метод объекта (instance method): работает с конкретным экземпляром
    def format_date(self) -> str:
        return f"{self.day:02d}/{self.month:02d}/{self.year}"

    # Метод класса (classmethod): альтернативный конструктор
    @classmethod
    def from_string(cls, date_str: str) -> Self:
        # Ожидает строку формата "ДД-ММ-ГГГГ"
        day, month, year = map(int, date_str.split("-"))
        return cls(day, month, year)

    # Статический метод (staticmethod): независимая утилита
    @staticmethod
    def is_valid_year(year: int) -> bool:
        return 1900 <= year <= 2100


# date1 = DateConverter(25, 5, 2026)
# print(date1.format_date())  # 25/05/2026

date2 = DateConverter.from_string("12-10-2024")
# print(date2.format_date())  # 12/10/2024

print(DateConverter.is_valid_year(2026))  # True
