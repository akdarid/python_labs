import os
import sys

LABA_03_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "laba_03"))
sys.path.insert(0, LABA_03_PATH)

from src.laba_07.models import SavingsAccount, CreditAccount

from collections import FunctionalBankAccountCollection
from strategies import (
    by_balance,
    by_owner_name,
    by_currency_and_balance,
    by_calculated_value,
    is_active,
    is_savings_account,
    is_credit_account,
    make_min_balance_filter,
    make_balance_range_filter,
    make_commission_applier,
    get_owner_name,
    to_short_string,
    to_dict,
    CurrentValueStrategy,
    CommissionStrategy,
    BonusPreviewStrategy,
)

def print_title(title: str) -> None:
    print(f"\n{'=' * 10} {title} {'=' * 10}")


def print_collection(collection: FunctionalBankAccountCollection) -> None:
    if len(collection) == 0:
        print("Коллекция пуста")
        return

    for item in collection:
        print(item)


def print_list(items: list) -> None:
    if not items:
        print("Список пуст")
        return

    for item in items:
        print(item)


def main() -> None:
    account1 = SavingsAccount("Иван Иванов", "SA1001", 1500.0, "RUB", 0.10, 100.0, True)
    account2 = CreditAccount("Мария Петрова", "CA2001", 2000.0, "USD", 5000.0, 300.0, True)
    account3 = SavingsAccount("Олег Смирнов", "SA1002", 3000.0, "EUR", 0.05, 50.0, True)
    account4 = CreditAccount("Анна Соколова", "CA2002", 800.0, "RUB", 3000.0, 100.0, False)
    account5 = SavingsAccount("Борис Орлов", "SA1003", 7000.0, "RUB", 0.07, 200.0, True)

    accounts = FunctionalBankAccountCollection()
    accounts.add(account1)
    accounts.add(account2)
    accounts.add(account3)
    accounts.add(account4)
    accounts.add(account5)

    print_title("Исходная коллекция")
    print_collection(accounts)

    print_title("Сценарий 1: сортировка тремя стратегиями")

    print("\nСортировка по балансу:")
    sorted_by_balance = sorted(accounts, key=by_balance)
    print_list(sorted_by_balance)

    print("\nСортировка по имени владельца:")
    sorted_by_name = accounts.sort_by(by_owner_name)
    print_collection(sorted_by_name)

    print("\nСортировка по валюте и балансу:")
    sorted_by_currency_balance = accounts.sort_by(by_currency_and_balance)
    print_collection(sorted_by_currency_balance)

    print_title("Сценарий 2: фильтрация через filter()")

    print("\nТолько активные счета:")
    active_accounts = list(filter(is_active, accounts))
    print_list(active_accounts)

    print("\nТолько накопительные счета:")
    savings_accounts = list(filter(is_savings_account, accounts))
    print_list(savings_accounts)

    print("\nТолько кредитные счета:")
    credit_accounts = list(filter(is_credit_account, accounts))
    print_list(credit_accounts)

    print_title("Сценарий 3: map(), lambda и фабрики функций")

    print("\nПолучение имён владельцев через map() и именованную функцию:")
    owner_names = list(map(get_owner_name, accounts))
    print_list(owner_names)

    print("\nПолучение имён владельцев через map() и lambda:")
    owner_names_lambda = list(map(lambda account: account.owner_name, accounts))
    print_list(owner_names_lambda)

    print("\nПреобразование счетов в короткие строки:")
    short_strings = list(map(to_short_string, accounts))
    print_list(short_strings)

    print("\nПреобразование счетов в словари:")
    account_dicts = list(map(to_dict, accounts))
    print_list(account_dicts)

    print("\nФабрика фильтра: счета с балансом от 1000 до 4000:")
    balance_filter = make_balance_range_filter(1000, 4000)
    filtered_by_range = accounts.filter_by(balance_filter)
    print_collection(filtered_by_range)

    print("\nФабрика функции: баланс после комиссии 10%:")
    commission_10 = make_commission_applier(0.10)
    after_commission = accounts.apply(commission_10)
    print_list(after_commission)

    print_title("Сценарий 4: цепочка filter -> sort -> apply")

    print("\nШаг 1. Исходная коллекция:")
    print_collection(accounts)

    print("\nШаг 2. После filter_by(is_active):")
    only_active = accounts.filter_by(is_active)
    print_collection(only_active)

    print("\nШаг 3. После sort_by(by_calculated_value, reverse=True):")
    sorted_active = only_active.sort_by(by_calculated_value, reverse=True)
    print_collection(sorted_active)

    print("\nШаг 4. После apply(to_short_string):")
    result = sorted_active.apply(to_short_string)
    print_list(result)

    print_title("Сценарий 5: паттерн Стратегия через callable-объекты")

    current_value_strategy = CurrentValueStrategy()
    commission_strategy = CommissionStrategy(0.15)
    bonus_strategy = BonusPreviewStrategy(500.0)

    print("\nОдна коллекция, разные стратегии обработки:")

    print("\nCurrentValueStrategy:")
    current_values = accounts.apply(current_value_strategy)
    print_list(current_values)

    print("\nCommissionStrategy 15%:")
    values_after_commission = accounts.apply(commission_strategy)
    print_list(values_after_commission)

    print("\nBonusPreviewStrategy +500:")
    values_with_bonus = accounts.apply(bonus_strategy)
    print_list(values_with_bonus)

    print("\nЗамена стратегии без изменения кода коллекции:")
    selected_account = account5
    print(f"Счёт: {selected_account.account_number}")
    print("CurrentValueStrategy:", current_value_strategy(selected_account))
    print("CommissionStrategy:", commission_strategy(selected_account))
    print("BonusPreviewStrategy:", bonus_strategy(selected_account))

    print_title("Сценарий 6: lambda и именованная функция дают одинаковый результат")

    print("\nСортировка по балансу через именованную функцию:")
    named_sorted = accounts.sort_by(by_balance)
    print_collection(named_sorted)

    print("\nСортировка по балансу через lambda:")
    lambda_sorted = accounts.sort_by(lambda account: account.balance)
    print_collection(lambda_sorted)

    print("\nФильтрация по балансу через фабрику функций:")
    min_balance_filter = make_min_balance_filter(2000)
    print_collection(accounts.filter_by(min_balance_filter))

    print("\nФильтрация по балансу через lambda:")
    print_collection(accounts.filter_by(lambda account: account.balance >= 2000))


if __name__ == "__main__":
    main()