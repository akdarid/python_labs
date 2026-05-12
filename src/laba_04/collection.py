from interfaces import Printable, Comparable


class AccountCollection:
    def __init__(self) -> None:
        self._items: list[object] = []

    def add(self, item: object) -> None:
        self._items.append(item)

    def get_all(self) -> list[object]:
        return self._items.copy()

    def get_printable(self) -> "AccountCollection":
        new_collection = AccountCollection()

        for item in self._items:
            if isinstance(item, Printable):
                new_collection.add(item)

        return new_collection

    def get_comparable(self) -> "AccountCollection":
        new_collection = AccountCollection()

        for item in self._items:
            if isinstance(item, Comparable):
                new_collection.add(item)

        return new_collection

    def sort_by_compare(self) -> None:
        comparable_items = []

        for item in self._items:
            if isinstance(item, Comparable):
                comparable_items.append(item)

        comparable_items.sort(key=lambda item: item.calculate())
        self._items = comparable_items

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> object:
        return self._items[index]