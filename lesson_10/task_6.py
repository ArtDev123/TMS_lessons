class Temperature:
    def __init__(self, celsius_temp):
        self.celsius = celsius_temp  # Вызовет сеттер

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Ошибка: Температура не может быть ниже абсолютного нуля!")
        else:
            self.__celsius = value

    @celsius.deleter
    def celsius(self):
        print("Данные о температуре в Цельсиях удалены.")
        del self.__celsius


temp = Temperature(25)
print(f"Текущая температура: {temp.celsius}°C")
temp.celsius = -300  # Выведет ошибку из сеттера


# Добавь геттер для другой шкалы: Создайте свойство @property def fahrenheit(self),
# которое будет возвращать температуру в Фаренгейтах. (Формула для расчета: celsius * 9/5 + 32).
# Сделай так, чтобы значение вычислялось «на лету» на основе self.__celsius.

# Улучши обработку ошибок: Измени сеттер celsius, чтобы вместо обычного print("Ошибка: ...")
# он вызывал исключение raise ValueError("Температура не может быть ниже абсолютного нуля!").

# Добавь сеттер для Фаренгейтов: Напиши @fahrenheit.setter.
# Когда пользователь задает температуру в Фаренгейтах (например, temp.fahrenheit = 100),
# сеттер должен перевести это значение в Цельсии (Формула: (fahrenheit - 32) * 5/9) и сохранить результат,
# используя уже существующий сеттер self.celsius.
