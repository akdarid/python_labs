class AppError(Exception):
    """Базовое исключение приложения."""


class AccountNotFoundError(AppError):
    """Счёт не найден в коллекции."""


class DuplicateAccountError(AppError):
    """Счёт с таким номером уже существует."""


class InvalidAccountDataError(AppError):
    """Переданы некорректные данные банковского счёта."""


class StorageError(AppError):
    """Ошибка сохранения или загрузки данных."""