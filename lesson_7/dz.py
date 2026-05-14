import string

from enum import Enum


class Mode(Enum):
    ENC = "enc"
    DECR = "decr"


class Language(Enum):
    RU = "ru"
    EN = "en"


def caesar_cipher(text: str, shift: int, mode: Mode, language: Language) -> str:
    # 1. Определяем алфавит
    if language == Language.RU:
        alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    elif language == Language.EN:
        alphabet = alphabet = string.ascii_lowercase
    else:
        raise ValueError(f"Unsupported language: {language}")

    # 2. Обработка режима (Mode)
    if mode == Mode.ENC:
        actual_shift = shift
    elif mode == Mode.DECR:
        actual_shift = -shift
    else:
        # Это сработает, если кто-то передаст некорректное значение вне Enum
        raise ValueError(f"Unsupported mode: {mode}")

    n = len(alphabet)
    result: list[str] = []

    for char in text:
        is_upper = char.isupper()
        low_char = char.lower()

        if low_char in alphabet:
            idx = alphabet.find(low_char)
            # Применяем формулу: (x + n) % n
            new_idx = (idx + actual_shift) % n
            new_char = alphabet[new_idx]
            result.append(new_char.upper() if is_upper else new_char)
        else:
            result.append(char)

    return "".join(result)


# Тест
print(caesar_cipher("Тулеих !", 3, Mode.ENC, Language.RU))
