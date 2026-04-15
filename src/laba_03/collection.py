from base import BankAccount


class BankAccountCollection:
    def __init__(self) -> None:
        self._items: list[BankAccount] = []

    def add(self, item: BankAccount) -> None:
        if not isinstance(item, BankAccount):
            raise TypeError("Можно добавлять только объекты BankAccount")

        if self.find_by_account_number(item.account_number) is not None:
            raise ValueError(
                f"Счёт с номером {item.account_number} уже существует в коллекции"
            )

        self._items.append(item)

    def remove(self, item: BankAccount) -> None:
        if not isinstance(item, BankAccount):
            raise TypeError("Удалять можно только объект BankAccount")

        self._items.remove(item)

    def get_all(self) -> list[BankAccount]:
        return self._items.copy()

    def find_by_account_number(self, account_number: str) -> BankAccount | None:
        for item in self._items:
            if item.account_number == account_number:
                return item
        return None

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> BankAccount:
        return self._items[index]

    def get_active(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if item.is_active:
                new_collection.add(item)

        return new_collection

    def get_savings_accounts(self) -> "BankAccountCollection":
        from models import SavingsAccount

        new_collection = BankAccountCollection()

        for item in self._items:
            if isinstance(item, SavingsAccount):
                new_collection.add(item)

        return new_collection

    def get_credit_accounts(self) -> "BankAccountCollection":
        from models import CreditAccount

        new_collection = BankAccountCollection()

        for item in self._items:
            if isinstance(item, CreditAccount):
                new_collection.add(item)

        return new_collection

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция счетов пуста"

        return "\n".join(str(item) for item in self._items)

    def __repr__(self) -> str:
        return f"BankAccountCollection(items={self._items})"