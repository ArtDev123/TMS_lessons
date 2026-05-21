class Phone:
    def make_call(self):
        print("Звоню по сотовой сети...")

    def charge(self):
        print("Заряжаюсь от провода.")


class Camera:
    def take_photo(self):
        print("Делаю снимок 12 Мп.")


class SmartPhone(Phone, Camera):
    def charge(self):
        print("Быстрая зарядка Type-C.")


iphone = SmartPhone()
iphone.take_photo()
iphone.make_call()
iphone.charge()


# Создай класс WirelessChargingMixin, в котором есть метод charge, печатающий "Заряжаюсь без проводов".

# Сделай так, чтобы SmartPhone наследовался от WirelessChargingMixin, Phone и Camera таким образом, чтобы при вызове iphone.charge() срабатывал метод из WirelessChargingMixin (Удалите метод charge из самого класса SmartPhone).

# Выведи в консоль SmartPhone.__mro__ и объясните соседу/преподавателю, почему при вызове charge() сработал именно этот метод (линеаризация).
