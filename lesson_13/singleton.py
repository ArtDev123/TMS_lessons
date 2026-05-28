from typing import Self, Any


class DatabaseConnection:
    _instance: Self | None = None  # Хранилище для единственного объекта

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if cls._instance is None:
            # Если объекта еще нет — создаем его
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_name: str) -> None:
        # Инициализацию нужно контролировать, чтобы не перезаписать данные
        if not hasattr(self, "initialized"):
            self.db_name = db_name
            self.initialized = True


# Демонстрация:
db1 = DatabaseConnection("Main_DB")
db2 = DatabaseConnection("Secondary_DB")

print(db1.db_name)  # Main_DB
print(db2.db_name)  # Main_DB (новый объект не создался!)
print(db1 is db2)  # True (это абсолютно один и тот же объект в памяти)
