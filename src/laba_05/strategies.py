def by_balance(account):
    """Стратегия сортировки по текущему балансу."""
    return account.balance


def by_owner_name(account):
    """Стратегия сортировки по имени владельца."""
    return account.owner_name.lower()


def by_currency_and_balance(account):
    """Стратегия сортировки по валюте и балансу одновременно."""
    return account.currency, account.balance


def by_calculated_value(account):
    """Стратегия сортировки по результату метода calculate()."""
    return account.calculate()


def is_active(account):
    """Фильтр: возвращает True, если счёт активен."""
    return account.is_active


def is_savings_account(account):
    """Фильтр: возвращает True, если объект является накопительным счётом."""
    return account.__class__.__name__ == "SavingsAccount"


def is_credit_account(account):
    """Фильтр: возвращает True, если объект является кредитным счётом."""
    return account.__class__.__name__ == "CreditAccount"


def make_min_balance_filter(min_balance):
    """
    Фабрика функций.
    Создаёт фильтр, который оставляет счета с балансом не меньше заданного.
    """
    def filter_fn(account):
        return account.balance >= min_balance

    return filter_fn


def make_balance_range_filter(min_balance, max_balance):
    """
    Фабрика функций.
    Создаёт фильтр по диапазону баланса.
    """
    def filter_fn(account):
        return min_balance <= account.balance <= max_balance

    return filter_fn


def get_owner_name(account):
    """Возвращает имя владельца счёта."""
    return account.owner_name


def to_short_string(account):
    """Преобразует объект счёта в короткую строку."""
    return f"{account.account_number}: {account.owner_name} ({account.balance:.2f} {account.currency})"


def to_dict(account):
    """Преобразует объект счёта в словарь."""
    return {
        "owner_name": account.owner_name,
        "account_number": account.account_number,
        "balance": account.balance,
        "currency": account.currency,
        "is_active": account.is_active,
        "calculated_value": account.calculate(),
    }


def make_commission_applier(percent):
    """
    Фабрика функций.
    Создаёт функцию, которая рассчитывает баланс после комиссии.
    """
    def apply_commission(account):
        commission = account.balance * percent
        return account.balance - commission

    return apply_commission


class CurrentValueStrategy:
    """Callable-стратегия: возвращает расчётное значение счёта."""

    def __call__(self, account):
        return account.calculate()


class CommissionStrategy:
    """Callable-стратегия: рассчитывает баланс после комиссии."""

    def __init__(self, percent):
        self.percent = percent

    def __call__(self, account):
        return account.balance - account.balance * self.percent


class BonusPreviewStrategy:
    """Callable-стратегия: показывает баланс с дополнительным бонусом."""

    def __init__(self, bonus):
        self.bonus = bonus

    def __call__(self, account):
        return account.balance + self.bonus