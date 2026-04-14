from model import BankAccount


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

    def remove_at(self, index: int) -> None:
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")

        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")

        self._items.pop(index)

    def get_all(self) -> list[BankAccount]:
        return self._items.copy()

    def find_by_account_number(self, account_number: str) -> BankAccount | None:
        for item in self._items:
            if item.account_number == account_number:
                return item
        return None

    def find_by_owner_name(self, owner_name: str) -> list[BankAccount]:
        result = []

        for item in self._items:
            if item.owner_name.lower() == owner_name.lower():
                result.append(item)

        return result

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> BankAccount:
        return self._items[index]

    def sort(self, key=None, reverse: bool = False) -> None:
        self._items.sort(key=key, reverse=reverse)

    def sort_by_owner_name(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda item: item.owner_name.lower(), reverse=reverse)

    def sort_by_balance(self, reverse: bool = False) -> None:
        self._items.sort(key=lambda item: item.balance, reverse=reverse)

    def get_active(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if item.is_active:
                new_collection.add(item)

        return new_collection

    def get_inactive(self) -> "BankAccountCollection":
        new_collection = BankAccountCollection()

        for item in self._items:
            if not item.is_active:
                new_collection.add(item)

        return new_collection

    def get_with_balance_more_than(self, amount: float) -> "BankAccountCollection":
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")

        new_collection = BankAccountCollection()

        for item in self._items:
            if item.balance > amount:
                new_collection.add(item)

        return new_collection

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция счетов пуста"

        return "\n".join(str(item) for item in self._items)

    def __repr__(self) -> str:
        return f"BankAccountCollection(items={self._items})"