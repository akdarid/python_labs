from __future__ import annotations

from typing import Callable, Sequence

from app import BankConsoleApp, SortStrategy
from exceptions import AppError
from base import BankAccount
from models import CreditAccount, SavingsAccount


class BankCLI:
    """Консольный интерфейс банковского приложения."""

    def __init__(self, app: BankConsoleApp) -> None:
        """Создать CLI-объект для работы с приложением."""
        self._app = app
        self._actions: dict[int, Callable[[], None]] = {
            1: self._add_savings_account,
            2: self._add_credit_account,
            3: self._show_all_accounts,
            4: self._find_account,
            5: self._filter_active_accounts,
            6: self._filter_by_currency,
            7: self._filter_by_balance_range,
            8: self._sort_accounts,
            9: self._delete_account,
            10: self._save_data,
        }

    def run(self) -> None:
        """Запустить цикл главного меню."""
        print("Банковское CLI-приложение запущено.")
        print("Данные автоматически загружены из файла.")

        while True:
            self._print_menu()

            try:
                choice = self._read_int("Выберите пункт: ")
            except ValueError:
                print("Ошибка: введите число.")
                continue

            if choice == 0:
                self._exit()
                break

            action = self._actions.get(choice)

            if action is None:
                print("Ошибка: такого пункта меню нет.")
                continue

            try:
                action()
            except AppError as error:
                print(f"Ошибка приложения: {error}")
            except ValueError as error:
                print(f"Ошибка ввода: {error}")
            except TypeError as error:
                print(f"Ошибка типа данных: {error}")

    def _print_menu(self) -> None:
        print("\n" + "=" * 50)
        print("МЕНЮ")
        print("=" * 50)
        print("1. Добавить накопительный счёт")
        print("2. Добавить кредитный счёт")
        print("3. Показать все счета")
        print("4. Найти счёт по номеру")
        print("5. Показать только активные счета")
        print("6. Фильтр по валюте")
        print("7. Фильтр по диапазону баланса")
        print("8. Сортировка")
        print("9. Удалить счёт")
        print("10. Сохранить данные")
        print("0. Выход")

    def _add_savings_account(self) -> None:
        print("\nДобавление накопительного счёта")

        owner_name = input("Владелец: ")
        account_number = input("Номер счёта: ")
        balance = self._read_float("Баланс: ")
        currency = input("Валюта: ")
        interest_rate = self._read_float("Процентная ставка, например 0.1: ")
        bonus = self._read_float("Бонус: ")

        account = self._app.add_savings_account(
            owner_name,
            account_number,
            balance,
            currency,
            interest_rate,
            bonus,
        )

        print("Накопительный счёт добавлен:")
        self._print_accounts([account])

    def _add_credit_account(self) -> None:
        print("\nДобавление кредитного счёта")

        owner_name = input("Владелец: ")
        account_number = input("Номер счёта: ")
        balance = self._read_float("Баланс: ")
        currency = input("Валюта: ")
        credit_limit = self._read_float("Кредитный лимит: ")
        debt = self._read_float("Текущий долг: ")

        account = self._app.add_credit_account(
            owner_name,
            account_number,
            balance,
            currency,
            credit_limit,
            debt,
        )

        print("Кредитный счёт добавлен:")
        self._print_accounts([account])

    def _show_all_accounts(self) -> None:
        print("\nВсе счета:")
        self._print_accounts(self._app.get_all_accounts())

    def _find_account(self) -> None:
        account_number = input("Введите номер счёта: ")
        account = self._app.find_account(account_number)

        print("\nНайденный счёт:")
        self._print_accounts([account])

    def _filter_active_accounts(self) -> None:
        print("\nАктивные счета:")
        self._print_accounts(self._app.filter_active_accounts())

    def _filter_by_currency(self) -> None:
        currency = input("Введите валюту, например RUB/USD/EUR: ")

        print(f"\nСчета в валюте {currency.upper()}:")
        self._print_accounts(self._app.filter_by_currency(currency))

    def _filter_by_balance_range(self) -> None:
        min_balance = self._read_float("Минимальный баланс: ")
        max_balance = self._read_float("Максимальный баланс: ")

        print("\nСчета в заданном диапазоне баланса:")
        self._print_accounts(
            self._app.filter_by_balance_range(min_balance, max_balance)
        )

    def _sort_accounts(self) -> None:
        print("\nСортировать по:")
        print("1. Имени владельца")
        print("2. Балансу")
        print("3. Валюте и балансу")
        print("4. Расчётному значению calculate()")

        choice = self._read_int("Выберите стратегию: ")
        reverse = self._confirm("Сортировать по убыванию?")

        strategies: dict[int, SortStrategy] = {
            1: "owner_name",
            2: "balance",
            3: "currency_and_balance",
            4: "calculated_value",
        }

        strategy = strategies.get(choice)

        if strategy is None:
            print("Ошибка: такой стратегии нет.")
            return

        sorted_accounts = self._app.sort_accounts(strategy, reverse)

        print("\nКоллекция отсортирована:")
        self._print_accounts(sorted_accounts)

    def _delete_account(self) -> None:
        account_number = input("Введите номер счёта для удаления: ")
        account = self._app.find_account(account_number)

        print("\nБудет удалён счёт:")
        self._print_accounts([account])

        if not self._confirm(f"Удалить счёт {account.account_number}?"):
            print("Удаление отменено.")
            return

        deleted_account = self._app.delete_account(account_number)
        print(f"Счёт {deleted_account.account_number} удалён.")

    def _save_data(self) -> None:
        self._app.save()
        print("Данные сохранены.")

    def _exit(self) -> None:
        self._app.save()
        print("Данные автоматически сохранены.")
        print("Выход из приложения.")

    def _print_accounts(self, accounts: Sequence[BankAccount]) -> None:
        if not accounts:
            print("Список пуст.")
            return

        header = (
            f"{'Тип':<14} | "
            f"{'Номер':<10} | "
            f"{'Владелец':<20} | "
            f"{'Баланс':>12} | "
            f"{'Валюта':<6} | "
            f"{'Активен':<8} | "
            f"{'Расчёт':>12}"
        )

        print(header)
        print("-" * len(header))

        for account in accounts:
            account_type = self._get_account_type(account)
            active = "да" if account.is_active else "нет"

            print(
                f"{account_type:<14} | "
                f"{account.account_number:<10} | "
                f"{account.owner_name:<20} | "
                f"{account.balance:>12.2f} | "
                f"{account.currency:<6} | "
                f"{active:<8} | "
                f"{account.calculate():>12.2f}"
            )

    def _get_account_type(self, account: BankAccount) -> str:
        if isinstance(account, SavingsAccount):
            return "Накопит."

        if isinstance(account, CreditAccount):
            return "Кредит."

        return "Базовый"

    def _read_int(self, prompt: str) -> int:
        value = input(prompt)
        return int(value)

    def _read_float(self, prompt: str) -> float:
        value = input(prompt)
        return float(value)

    def _confirm(self, question: str) -> bool:
        answer = input(f"{question} (y/n): ").strip().lower()
        return answer in ("y", "yes", "д", "да")