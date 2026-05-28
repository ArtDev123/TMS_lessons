import os
from abc import ABC, abstractmethod

DEFAULT_CONFIG = {"mode": "console"}


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[Console]: {message}")


class FileLogger(Logger):
    def log(self, message: str) -> None:
        print(f"[File]: Записано в файл: {message}")


class DatabaseLogger:
    def log(self, message: str) -> None:
        print(f"[Database]: {message}")


class LoggerFactory:
    @staticmethod
    def get_logger(
        mode: str | None = None,
    ) -> Logger:
        if mode is None:
            mode = os.environ.get("LOG_MODE", DEFAULT_CONFIG["mode"])

        if mode == "console":
            return ConsoleLogger()
        if mode == "file":
            return FileLogger()
        if mode == "db":
            return DatabaseLogger()

        raise ValueError(f"Неизвестный режим логгера: {mode}")


LoggerFactory.get_logger("console").log("Сообщение в консоль")
LoggerFactory.get_logger("file").log("Сообщение в файл")
LoggerFactory.get_logger("db").log("Сообщение в БД")

logger_from_config = LoggerFactory.get_logger()
logger_from_config.log("Режим из DEFAULT_CONFIG")

os.environ["LOG_MODE"] = "file"
logger_from_env = LoggerFactory.get_logger()
logger_from_env.log("Режим из переменной окружения")

try:
    LoggerFactory.get_logger("unknown")
except ValueError as e:
    print(e)
