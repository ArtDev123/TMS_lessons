import re

log_data = """
2023-10-15: User from 192.168.0.1 failed to login. ERROR.
2023-10-16: User from 10.0.0.55 logged in successfully. INFO.
2023-10-17: Server at 127.0.0.1 restarted. ERROR.
"""

# TODO 1: Напиши регулярное выражение и найди все даты в формате ГГГГ-ММ-ДД.
dates = []  # Добавь re.findall

# TODO 2: Напиши регулярное выражение и найди все IP-адреса (формат: число.число.число.число).
ips = []  # Добавь re.findall

# TODO 3: Используй re.sub, чтобы заменить в тексте log_data все слова "ERROR" на "WARNING",
# и выведи исправленный текст на экран.
fixed_log = ""
