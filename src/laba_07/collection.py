from base import BankAccount


class BankAccountCollection:
    def __init__(self) -> None:
        self._items: list[BankAccount] = []

    def _is_bank_account_like(self, item: object) -> bool:
        """Проверить, что объект похож на банковский счёт."""
        required_attributes = (
            "owner_name",
            "account_number",
            "balance",
            "currency",
            "is_active",
            "calculate",
        )

        return all(hasattr(item, attr) for attr in required_attributes)

    def add(self, item: BankAccount) -> None:
        if not self._is_bank_account_like(item):
            raise TypeError("Можно добавлять только объекты банковских счетов")

        if self.find_by_account_number(item.account_number) is not None:
            raise ValueError(
                f"Счёт с номером {item.account_number} уже существует в коллекции"
            )

        self._items.append(item)

    def remove(self, item: BankAccount) -> None:
        if item not in self._items:
            raise ValueError("Такого объекта нет в коллекции")

        self._items.remove(item)

    def get_all(self) -> list[BankAccount]:
        return self._items.copy()

    def find_by_account_number(self, account_number: str) -> BankAccount | None:
        for item in self._items:
            if item.account_number == account_number:
                return item

        return None

    def get_active(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if item.is_active:
                new_collection.add(item)

        return new_collection

    def get_savings_accounts(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if item.__class__.__name__ == "SavingsAccount":
                new_collection.add(item)

        return new_collection

    def get_credit_accounts(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if item.__class__.__name__ == "CreditAccount":
                new_collection.add(item)

        return new_collection

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> BankAccount:
        return self._items[index]

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция счетов пуста"

        return "\n".join(str(item) for item in self._items)

    def __repr__(self) -> str:
        return f"BankAccountCollection(items={self._items})"