from model import BankAccount
from collection import BankAccountCollection


def print_title(title: str) -> None:
    print(f"\n{'=' * 10} {title} {'=' * 10}")


def print_collection(collection: BankAccountCollection) -> None:
    if len(collection) == 0:
        print("Коллекция пуста")
        return

    for item in collection:
        print(item)


def main() -> None:
    account1 = BankAccount("Иван Иванов", "ACC1001", 1500.0, "RUB", True)
    account2 = BankAccount("Мария Петрова", "ACC1002", 3200.5, "USD", True)
    account3 = BankAccount("Алексей Смирнов", "ACC1003", 500.0, "EUR", False)
    account4 = BankAccount("Иван Иванов", "ACC1004", 8000.0, "RUB", True)

    accounts = BankAccountCollection()

    print_title("Добавление объектов")
    accounts.add(account1)
    accounts.add(account2)
    accounts.add(account3)
    accounts.add(account4)
    print_collection(accounts)

    print_title("Вывод через get_all()")
    for item in accounts.get_all():
        print(item)

    print_title("Поиск по номеру счёта")
    found = accounts.find_by_account_number("ACC1002")
    print(found if found is not None else "Счёт не найден")

    print_title("Поиск по владельцу")
    found_by_owner = accounts.find_by_owner_name("Иван Иванов")
    for item in found_by_owner:
        print(item)

    print_title("Использование len()")
    print(f"Количество счетов в коллекции: {len(accounts)}")

    print_title("Итерация по коллекции")
    for account in accounts:
        print(account)

    print_title("Индексация")
    print(accounts[0])
    print(accounts[2])

    print_title("Проверка запрета дубликатов")
    duplicate = BankAccount("Другой владелец", "ACC1001", 999.0, "RUB", True)
    try:
        accounts.add(duplicate)
    except ValueError as error:
        print(f"Ошибка: {error}")

    print_title("Сортировка по имени владельца")
    accounts.sort_by_owner_name()
    print_collection(accounts)

    print_title("Сортировка по балансу по убыванию")
    accounts.sort_by_balance(reverse=True)
    print_collection(accounts)

    print_title("Фильтрация: активные счета")
    active_accounts = accounts.get_active()
    print_collection(active_accounts)

    print_title("Фильтрация: неактивные счета")
    inactive_accounts = accounts.get_inactive()
    print_collection(inactive_accounts)

    print_title("Фильтрация: баланс больше 1000")
    rich_accounts = accounts.get_with_balance_more_than(1000)
    print_collection(rich_accounts)

    print_title("Удаление объекта")
    accounts.remove(account2)
    print_collection(accounts)

    print_title("Удаление по индексу")
    accounts.remove_at(0)
    print_collection(accounts)

    print_title("Сценарии использования")

    print("\nСценарий 1: Получение всех активных счетов")
    active = accounts.get_active()
    print_collection(active)

    print("\nСценарий 2: Сортировка счетов по балансу")
    accounts.sort_by_balance()
    print_collection(accounts)

    print("\nСценарий 3: Поиск счёта по номеру")
    result = accounts.find_by_account_number("ACC1003")
    print(result if result is not None else "Счёт не найден")


if __name__ == "__main__":
    main()