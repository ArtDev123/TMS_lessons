from typing import Any


class NewsAgency:
    """Издатель (Subject): рассылает уведомления подписчикам."""

    def __init__(self) -> None:
        self._subscribers = []

    def subscribe(self, subscriber: Any) -> None:
        self._subscribers.append(subscriber)

    def notify_all(self, news: Any) -> None:
        for sub in self._subscribers:
            sub.update(news)


# Реализация подписчиков (Полиморфизм паттерна):
# Создай два класса подписчиков: EmailSubscriber(name) и SMSSubscriber(phone).
# У каждого должен быть метод update(self, news), выводящий индивидуальное
# сообщение в консоль (например: «Email для Ивана: Новая новость: ...»).
# Протестируй подписку и рассылку.

# Интеграция Итератора:
# Модифицируй класс NewsAgency так, чтобы сам объект агентства
# стал итерируемым (реализуйте протокол __iter__ / __next__). Каждая итерация по агентству
# должна выдавать подписчиков по очереди. То есть, чтобы можно было написать: for sub in agency: print(sub).

# Умный архив через генератор:
# Добавь в NewsAgency хранилище истории новостей self.news_history.
# Напиши метод-генератор news_archive_filter(self, keyword),
# который лениво (через yield) просматривает историю и выдает только те новости,
# которые содержат ключевое слово keyword.
# Продемонстрируй, как подписчик может затребовать из архива выборочные новости,
# не загружая всю историю в память смартфона или ПК.
