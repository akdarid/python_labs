from collection import BankAccountCollection
from models import SavingsAccount, CreditAccount


def print_title(title: str) -> None:
    print(f"\n{'=' * 10} {title} {'=' * 10}")


def print_collection(collection: BankAccountCollection) -> None:
    if len(collection) == 0:
        print("Коллекция пуста")
        return

    for item in collection:
        print(item)


def main() -> None:
    savings1 = SavingsAccount(
        "Иван Иванов",
        "SA1001",
        1500.0,
        "RUB",
        0.10,
        100.0,
        True
    )

    credit1 = CreditAccount(
        "Мария Петрова",
        "CA2001",
        2000.0,
        "USD",
        5000.0,
        300.0,
        True
    )

    savings2 = SavingsAccount(
        "Олег Смирнов",
        "SA1002",
        3000.0,
        "EUR",
        0.05,
        50.0,
        True
    )

    accounts = BankAccountCollection()

    accounts.add(savings1)
    accounts.add(credit1)
    accounts.add(savings2)

    print_title("Все объекты в одной коллекции")
    print_collection(accounts)

    print_title("Использование базовых методов")
    savings1.deposit(500.0)
    credit1.withdraw(200.0)
    print(savings1)
    print(credit1)

    print_title("Использование дочерних методов")
    savings1.apply_interest()
    credit1.take_credit(400.0)
    print(savings1)
    print(credit1)

    print_title("Проверка типов через isinstance()")
    for account in accounts:
        if isinstance(account, SavingsAccount):
            print(f"Накопительный счёт: {account.account_number}")

        if isinstance(account, CreditAccount):
            print(f"Кредитный счёт: {account.account_number}")

    print_title("Полиморфизм: один метод calculate() — разное поведение")
    for account in accounts:
        print(f"{account.account_number}: {account.calculate():.2f} {account.currency}")

    print_title("Фильтрация: только накопительные счета")
    print_collection(accounts.get_savings_accounts())

    print_title("Фильтрация: только кредитные счета")
    print_collection(accounts.get_credit_accounts())

    print_title("Фильтрация: только активные счета")
    print_collection(accounts.get_active())

    print_title("Сценарий 1: начисление процентов и бонуса")
    print("До:", savings2)
    savings2.apply_interest()
    savings2.add_bonus()
    print("После:", savings2)

    print_title("Сценарий 2: оформление и погашение кредита")
    print("До:", credit1)
    credit1.take_credit(300.0)
    credit1.repay_credit(200.0)
    print("После:", credit1)

    print_title("Сценарий 3: единый вызов calculate() для всех объектов")
    for account in accounts:
        print(f"{account.owner_name}: {account.calculate():.2f} {account.currency}")


if __name__ == "__main__":
    main()