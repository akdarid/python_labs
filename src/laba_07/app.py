from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Literal, Sequence


CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent

for path in (
    SRC_DIR / "lab03",
    SRC_DIR / "laba_03",
):
    if path.exists() and str(path) not in sys.path:
        sys.path.insert(0, str(path))


from base import BankAccount
from collection import BankAccountCollection
from models import CreditAccount, SavingsAccount

from exceptions import (
    AccountNotFoundError,
    DuplicateAccountError,
    InvalidAccountDataError,
)
from storage import load_accounts, save_accounts


SortStrategy = Literal[
    "owner_name",
    "balance",
    "currency_and_balance",
    "calculated_value",
]


class BankConsoleApp:
    """Слой бизнес-логики консольного приложения."""

    def __init__(self, data_file: Path, autoload: bool = True) -> None:
        """Создать приложение и при необходимости загрузить данные."""
        self._data_file = data_file
        self._collection = BankAccountCollection()

        if autoload:
            self.load()

    def load(self) -> None:
        """Загрузить счета из файла в коллекцию."""
        self._collection = BankAccountCollection()

        for account in load_accounts(self._data_file):
            self._collection.add(account)

    def save(self) -> None:
        """Сохранить текущую коллекцию счетов в файл."""
        save_accounts(self.get_all_accounts(), self._data_file)

    def add_savings_account(
        self,
        owner_name: str,
        account_number: str,
        balance: float,
        currency: str,
        interest_rate: float,
        bonus: float,
    ) -> SavingsAccount:
        """Добавить накопительный счёт в коллекцию."""
        self._ensure_unique_account_number(account_number)
        self._validate_non_negative(interest_rate, "Процентная ставка")
        self._validate_non_negative(bonus, "Бонус")

        account = SavingsAccount(
            owner_name,
            account_number,
            balance,
            currency,
            interest_rate,
            bonus,
        )

        self._collection.add(account)
        return account

    def add_credit_account(
        self,
        owner_name: str,
        account_number: str,
        balance: float,
        currency: str,
        credit_limit: float,
        debt: float,
    ) -> CreditAccount:
        """Добавить кредитный счёт в коллекцию."""
        self._ensure_unique_account_number(account_number)
        self._validate_non_negative(credit_limit, "Кредитный лимит")
        self._validate_non_negative(debt, "Долг")

        if debt > credit_limit:
            raise InvalidAccountDataError(
                "Долг не может быть больше кредитного лимита"
            )

        account = CreditAccount(
            owner_name,
            account_number,
            balance,
            currency,
            credit_limit,
            debt,
        )

        self._collection.add(account)
        return account

    def get_all_accounts(self) -> list[BankAccount]:
        """Получить все счета из коллекции."""
        return self._collection.get_all()

    def find_account(self, account_number: str) -> BankAccount:
        """Найти счёт по номеру."""
        account = self._collection.find_by_account_number(account_number)

        if account is None:
            raise AccountNotFoundError(
                f"Счёт с номером {account_number} не найден"
            )

        return account

    def delete_account(self, account_number: str) -> BankAccount:
        """Удалить счёт по номеру и вернуть удалённый объект."""
        account = self.find_account(account_number)
        self._collection.remove(account)
        return account

    def filter_active_accounts(self) -> list[BankAccount]:
        """Получить только активные счета."""
        return self._collection.get_active().get_all()

    def filter_by_currency(self, currency: str) -> list[BankAccount]:
        """Получить счета в указанной валюте."""
        normalized_currency = currency.strip().upper()

        return [
            account
            for account in self.get_all_accounts()
            if account.currency == normalized_currency
        ]

    def filter_by_balance_range(
        self,
        min_balance: float,
        max_balance: float,
    ) -> list[BankAccount]:
        """Получить счета, баланс которых находится в заданном диапазоне."""
        if min_balance > max_balance:
            raise InvalidAccountDataError(
                "Минимальный баланс не может быть больше максимального"
            )

        return [
            account
            for account in self.get_all_accounts()
            if min_balance <= account.balance <= max_balance
        ]

    def sort_accounts(
        self,
        strategy: SortStrategy,
        reverse: bool = False,
    ) -> list[BankAccount]:
        """Отсортировать коллекцию по выбранной стратегии."""
        key_func = self._get_sort_key(strategy)

        sorted_accounts = sorted(
            self.get_all_accounts(),
            key=key_func,
            reverse=reverse,
        )

        self._replace_collection(sorted_accounts)
        return sorted_accounts

    def _ensure_unique_account_number(self, account_number: str) -> None:
        account = self._collection.find_by_account_number(account_number)

        if account is not None:
            raise DuplicateAccountError(
                f"Счёт с номером {account_number} уже существует"
            )

    def _replace_collection(self, accounts: Sequence[BankAccount]) -> None:
        self._collection = BankAccountCollection()

        for account in accounts:
            self._collection.add(account)

    def _get_sort_key(
        self,
        strategy: SortStrategy,
    ) -> Callable[[BankAccount], object]:
        if strategy == "owner_name":
            return lambda account: account.owner_name.lower()

        if strategy == "balance":
            return lambda account: account.balance

        if strategy == "currency_and_balance":
            return lambda account: (account.currency, account.balance)

        if strategy == "calculated_value":
            return lambda account: account.calculate()

        raise InvalidAccountDataError("Неизвестная стратегия сортировки")

    def _validate_non_negative(self, value: float, field_name: str) -> None:
        if value < 0:
            raise InvalidAccountDataError(
                f"{field_name} не может быть отрицательным"
            )