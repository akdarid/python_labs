from src.laba_01.validate  import (
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

    @balance.setter
    def balance(self, value: float) -> None:
        self._balance = validate_balance(value)

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def is_active(self) -> bool:
        return self._is_active

    def deposit(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self._is_active:
            raise ValueError("Нельзя пополнить неактивный счёт")

        self._balance += amount

    def withdraw(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self._is_active:
            raise ValueError("Нельзя снимать деньги с неактивного счёта")

        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")

        self._balance -= amount

    def can_withdraw(self, amount: float) -> bool:
        try:
            amount = validate_amount(amount)
        except (TypeError, ValueError):
            return False

        if not self._is_active:
            return False

        return amount <= self._balance

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def __str__(self) -> str:
        status: str = "активен" if self._is_active else "неактивен"
        return (
            f"Счёт {self._account_number} | "
            f"Владелец: {self._owner_name} | "
            f"Баланс: {self._balance:.2f} {self._currency} | "
            f"Статус: {status}"
        )

    def __repr__(self) -> str:
        return (
            f"BankAccount("
            f"owner_name='{self._owner_name}', "
            f"account_number='{self._account_number}', "
            f"balance={self._balance}, "
            f"currency='{self._currency}', "
            f"is_active={self._is_active})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BankAccount):
            return False

        return self._account_number == other._account_number