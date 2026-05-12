from interfaces import Printable, Comparable
from models import SavingsAccount, CreditAccount
from collection import AccountCollection


def print_title(title: str) -> None:
    print(f"\n{'=' * 10} {title} {'=' * 10}")


# Универсальная функция через интерфейс Printable
def print_all(items: list[Printable]) -> None:
    for item in items:
        print(item.to_string())


# Универсальная функция через интерфейс Comparable
def compare_accounts(first: Comparable, second: Comparable) -> None:
    result = first.compare_to(second)

    if result > 0:
        print("Первый объект больше второго")

    elif result < 0:
        print("Первый объект меньше второго")

    else:
        print("Объекты равны")


def main() -> None:
    savings1 = SavingsAccount(
        "Иван Иванов",
        "SA1001",
        1500.0,
        "RUB",
        0.10,
        100.0
    )

    credit1 = CreditAccount(
        "Мария Петрова",
        "CA2001",
        2000.0,
        "USD",
        5000.0,
        300.0
    )

    savings2 = SavingsAccount(
        "Олег Смирнов",
        "SA1002",
        3000.0,
        "EUR",
        0.05,
        50.0
    )

    accounts = AccountCollection()

    accounts.add(savings1)
    accounts.add(credit1)
    accounts.add(savings2)

    # =========================================================
    # СЦЕНАРИЙ 1
    # =========================================================

    print_title("Сценарий 1: Проверка интерфейсов")

    for account in accounts:
        print(account.to_string())

        if isinstance(account, Printable):
            print("Реализует Printable")

        if isinstance(account, Comparable):
            print("Реализует Comparable")

        print()

    # =========================================================
    # СЦЕНАРИЙ 2
    # =========================================================

    print_title("Сценарий 2: Интерфейс как тип")

    print("Функция print_all() работает через Printable:\n")
    print_all(accounts.get_all())

    print("\nСравнение объектов через Comparable:\n")
    compare_accounts(savings1, credit1)

    # =========================================================
    # СЦЕНАРИЙ 3
    # =========================================================

    print_title("Сценарий 3: Полиморфизм и работа коллекции")

    print("Все объекты коллекции:\n")

    for account in accounts:
        print(account.to_string())

    print("\nФильтрация по интерфейсу Printable:\n")

    printable_accounts = accounts.get_printable()

    for account in printable_accounts:
        print(account.to_string())

    print("\nСортировка через Comparable:\n")

    accounts.sort_by_compare()

    for account in accounts:
        print(
            f"{account.account_number} -> "
            f"{account.calculate():.2f} {account.currency}"
        )


if __name__ == "__main__":
    main()