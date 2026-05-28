from dataclasses import dataclass
from typing import Self


@dataclass
class Hero:
    name: str
    hp: int
    attack_power: int

    def attack(self, other: Self) -> None:
        other.hp -= self.attack_power
        print(f"{self.name} атакует {other.name} на {self.attack_power} урона!")


# Добавь в Hero методы класса @classmethod для быстрого создания шаблонных персонажей:
# create_warrior(cls, name) (дает много HP, среднюю атаку) и create_mage(cls, name)
# (дает мало HP, но огромную атаку).

# Перегрузи оператор __sub__ (минус) для персонажей так,
# чтобы выражение hero1 - hero2 означало: "hero1 атакует hero2".
# Метод должен уменьшать здоровье hero2 на величину атаки hero1.
# Также перегрузи __bool__, чтобы проверка if hero: возвращала True,
# если персонаж жив (hp > 0), и False, если погиб.

# Создай класс Spell (Заклинание) и его наследников:
# Fireball (наносит фиксированный урон) и Heal (лечит выбранного героя, увеличивая его hp).
# Добавь героям-магам список заклинаний spells.
# Напиши симуляцию боя: цикл while,
# в котором два сгенерированных персонажа обмениваются ударами и используют полиморфные заклинания из списков,
# пока один из них не выключится (проверка через перегруженный __bool__).
