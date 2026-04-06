from model import BankAccount


def main() -> None:
    print("=== ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА BankAccount ===")

    print("\n1. Создание объекта:")
    account1 = BankAccount("Иван Иванов", "ACC123", 1000.0, "rub")
    print(account1)

    print("\n2. Техническое представление объекта (__repr__):")
    print(repr(account1))

    print("\n3. Создание второго объекта:")
    account2 = BankAccount("Пётр Петров", "ACC123", 500.0, "RUB")
    print(account2)

    print("\n4. Сравнение двух объектов (__eq__):")
    print("account1 == account2 ->", account1 == account2)

    print("\n5. Пополнение счёта:")
    account1.deposit(250.0)
    print(account1)

    print("\n6. Снятие денег:")
    account1.withdraw(300.0)
    print(account1)

    print("\n7. Проверка возможности снятия:")
    print("Можно снять 200?", account1.can_withdraw(200))
    print("Можно снять 5000?", account1.can_withdraw(5000))

    print("\n8. Изменение состояния счёта:")
    account1.deactivate()
    print(account1)

    print("\n9. Попытка выполнить операцию с неактивным счётом:")
    try:
        account1.deposit(100.0)
    except ValueError as error:
        print("Ошибка:", error)

    print("\n10. Повторная активация счёта:")
    account1.activate()
    print(account1)

    print("\n11. Атрибут класса:")
    print("Через класс:", BankAccount.bank_name)
    print("Через экземпляр:", account1.bank_name)

    print("\n12. Пример некорректного создания объекта:")
    try:
        bad_account = BankAccount("", "ACC999", -100, "RUB")
        print(bad_account)
    except (TypeError, ValueError) as error:
        print("Ошибка:", error)

    print("\n13. Пример некорректного снятия денег:")
    try:
        account1.withdraw(100000.0)
    except ValueError as error:
        print("Ошибка:", error)


if __name__ == "__main__":
    main()