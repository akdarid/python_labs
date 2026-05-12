from validate import (
    validate_owner_name,
    validate_account_number,
    validate_balance,
    validate_currency,
    validate_is_active,
    validate_amount,
)


class BankAccount:
    bank_name: str = "Arid's Bank"

    def __init__(
        self,
        owner_name: str,
        account_number: str,
        balance: float,
        currency: str,
        is_active: bool = True
    ) -> None:
        self._owner_name: str = validate_owner_name(owner_name)
        self._account_number: str = validate_account_number(account_number)
        self._balance: float = validate_balance(balance)
        self._currency: str = validate_currency(currency)
        self._is_active: bool = validate_is_active(is_active)

    @property
    def owner_name(self) -> str:
        return self._owner_name

    @property
    def account_number(self) -> str:
        return self._account_number

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def is_active(self) -> bool:
        return self._is_active

    # 🔥 общий интерфейс (для задания на 5)
    def calculate(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self._is_active:
            raise ValueError("Счёт неактивен")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self._is_active:
            raise ValueError("Счёт неактивен")

        if amount > self._balance:
            raise ValueError("Недостаточно средств")

        self._balance -= amount

    def __str__(self) -> str:
        return f"{self._account_number} | {self._owner_name} | {self._balance:.2f} {self._currency}"