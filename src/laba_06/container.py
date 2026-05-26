from typing import (
    TypeVar,
    Generic,
    Callable,
    Optional,
    Protocol,
    Iterator,
)

# ===== Protocol =====

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...


# ===== TypeVar =====

T = TypeVar("T")
R = TypeVar("R")

D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


# ===== Generic Collection =====

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def remove_at(self, index: int) -> None:
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")

        self._items.pop(index)

    def get_all(self) -> list[T]:
        return self._items.copy()

    def find(
        self,
        predicate: Callable[[T], bool]
    ) -> Optional[T]:

        for item in self._items:
            if predicate(item):
                return item

        return None

    def filter(
        self,
        predicate: Callable[[T], bool]
    ) -> list[T]:

        return [
            item
            for item in self._items
            if predicate(item)
        ]

    def map(
        self,
        transform: Callable[[T], R]
    ) -> list[R]:

        return [
            transform(item)
            for item in self._items
        ]

    def sort_by(
        self,
        key_func: Callable[[T], object],
        reverse: bool = False
    ) -> "TypedCollection[T]":

        self._items.sort(
            key=key_func,
            reverse=reverse
        )

        return self

    def filter_by(
        self,
        predicate: Callable[[T], bool]
    ) -> "TypedCollection[T]":

        new_collection = TypedCollection[T]()

        for item in self._items:
            if predicate(item):
                new_collection.add(item)

        return new_collection

    def apply(
        self,
        func: Callable[[T], R]
    ) -> list[R]:

        return [
            func(item)
            for item in self._items
        ]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __str__(self) -> str:
        if not self._items:
            return "Коллекция пуста"

        return "\n".join(str(item) for item in self._items)