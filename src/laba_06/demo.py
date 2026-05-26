from src.laba_06.container import (
    TypedCollection,
    D,
    S,
)

from src.laba_07.models import (
    SavingsAccount,
    CreditAccount,
)


def scenario_1() -> None:
    print("========== Сценарий 1 ==========")

    collection: TypedCollection[SavingsAccount] = TypedCollection()

    acc1 = SavingsAccount(
        "Иван",
        "SA001",
        10000,
        "RUB",
        0.1,
        500
    )

    acc2 = SavingsAccount(
        "Мария",
        "SA002",
        20000,
        "RUB",
        0.2,
        1000
    )

    collection.add(acc1)
    collection.add(acc2)

    for item in collection:
        print(item)


def scenario_2() -> None:
    print("\n========== Сценарий 2 ==========")

    collection: TypedCollection[SavingsAccount] = TypedCollection()

    acc1 = SavingsAccount(
        "Иван",
        "SA001",
        10000,
        "RUB",
        0.1,
        500
    )

    acc2 = SavingsAccount(
        "Мария",
        "SA002",
        20000,
        "RUB",
        0.2,
        1000
    )

    collection.add(acc1)
    collection.add(acc2)

    found = collection.find(
        lambda x: x.balance > 15000
    )

    print("Найден:")
    print(found)

    not_found = collection.find(
        lambda x: x.balance > 999999
    )

    print("\nНе найден:")
    print(not_found)

    filtered = collection.filter(
        lambda x: x.balance > 15000
    )

    print("\nФильтрация:")

    for item in filtered:
        print(item)

    names = collection.map(
        lambda x: x.owner_name
    )

    print("\nmap -> list[str]:")
    print(names)

    balances = collection.map(
        lambda x: x.balance
    )

    print("\nmap -> list[float]:")
    print(balances)


def scenario_3() -> None:
    print("\n========== Сценарий 3 ==========")

    collection: TypedCollection[D] = TypedCollection()

    acc1 = SavingsAccount(
        "Иван",
        "SA001",
        10000,
        "RUB",
        0.1,
        500
    )

    acc2 = CreditAccount(
        "Мария",
        "CR001",
        5000,
        "USD",
        10000,
        2000
    )

    collection.add(acc1)
    collection.add(acc2)

    for item in collection:
        print(item.display())


def scenario_4() -> None:
    print("\n========== Сценарий 4 ==========")

    collection: TypedCollection[S] = TypedCollection()

    acc1 = SavingsAccount(
        "Иван",
        "SA001",
        10000,
        "RUB",
        0.1,
        500
    )

    acc2 = CreditAccount(
        "Мария",
        "CR001",
        5000,
        "USD",
        10000,
        2000
    )

    collection.add(acc1)
    collection.add(acc2)

    for item in collection:
        print(
            item.owner_name,
            "->",
            item.score()
        )


if __name__ == "__main__":
    scenario_1()
    scenario_2()
    scenario_3()
    scenario_4()