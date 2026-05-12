class FunctionalBankAccountCollection:
    def __init__(self, items=None) -> None:
        self._items = list(items) if items is not None else []

    def add(self, item) -> None:
        self._items.append(item)

    def get_all(self) -> list:
        return self._items.copy()

    def sort_by(self, key_func, reverse: bool = False) -> "FunctionalBankAccountCollection":
        sorted_items = sorted(self._items, key=key_func, reverse=reverse)
        return FunctionalBankAccountCollection(sorted_items)

    def filter_by(self, predicate) -> "FunctionalBankAccountCollection":
        filtered_items = list(filter(predicate, self._items))
        return FunctionalBankAccountCollection(filtered_items)

    def apply(self, func) -> list:
        return list(map(func, self._items))

    def __iter__(self):
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __getitem__(self, index: int):
        return self._items[index]

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"

        return "\n".join(str(item) for item in self._items)