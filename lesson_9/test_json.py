import json

from typing import Any

user_data: dict[str, Any] = {
    "username": "admin",
    "is_active": True,
    "roles": ["read", "write"],
}

# Сериализация: сохраняем Python-словарь в JSON-файл
with open("user.json", "w", encoding="utf-8") as f:
    # indent=4 делает файл читаемым (с отступами)
    json.dump(user_data, f, indent=4)
    pass

# Десериализация: читаем из файла обратно в словарь
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print("Загруженные роли:", loaded_data["roles"])
