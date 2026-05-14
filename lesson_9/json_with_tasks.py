import json

raw_json_string = """
[
    {"name": "Alex", "age": 15},
    {"name": "Maria", "age": 22},
    {"name": "Ivan", "age": 18},
    {"name": "Nina", "age": 12}
]
"""

users = json.loads(raw_json_string)

adults = [user for user in users if user["age"] >= 18]

with open("adults.json", "w", encoding="utf-8") as file:
    json.dump(adults, file, indent=4)
