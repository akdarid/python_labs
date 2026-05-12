

from base import BankAccount
from interfaces import Printable, Comparable
from validate import (
    validate_owner_name,
    validate_account_number,
    validate_balance,
    validate_currency,
    validate_is_active,
    validate_amount,
)

class SavingsAccount(BankAccount, Printable, Comparable):
    def __init__(
        self,
        owner_name: str,
        account_number: str,
        balance: float,
        currency: str,
        interest_rate: float,
        bonus: float,
        is_active: bool = True
    ) -> None:
        super().__init__(owner_name, account_number, balance, currency, is_active)

        self.interest_rate = interest_rate
        self.bonus = bonus

    def apply_interest(self) -> None:
        if not self.is_active:
            raise ValueError("Нельзя начислить проценты на неактивный счёт")

        self._balance += self._balance * self.interest_rate

    def add_bonus(self) -> None:
        if not self.is_active:
            raise ValueError("Нельзя начислить бонус на неактивный счёт")

        self._balance += self.bonus

    def calculate(self) -> float:
        return self._balance + (self._balance * self.interest_rate) + self.bonus

    def to_string(self) -> str:
        return (
            f"Накопительный счёт | "
            f"Владелец: {self.owner_name} | "
            f"Номер: {self.account_number} | "
            f"Итоговая сумма: {self.calculate():.2f} {self.currency}"
        )

    def compare_to(self, other: object) -> int:
        if not isinstance(other, Comparable):
            raise TypeError("Сравнивать можно только с объектом Comparable")

        if self.calculate() > other.calculate():
            return 1

        if self.calculate() < other.calculate():
            return -1

        return 0

    def __str__(self) -> str:
        return (
            f"[Savings] {super().__str__()} | "
            f"ставка: {self.interest_rate} | бонус: {self.bonus}"
        )


class CreditAccount(BankAccount, Printable, Comparable):
    def __init__(
        self,
        owner_name: str,
        account_number: str,
        balance: float,
        currency: str,
        credit_limit: float,
        debt: float,
        is_active: bool = True
    ) -> None:
        super().__init__(owner_name, account_number, balance, currency, is_active)

        self.credit_limit = credit_limit
        self.debt = debt

    def take_credit(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self.is_active:
            raise ValueError("Нельзя взять кредит для неактивного счёта")

        if self.debt + amount > self.credit_limit:
            raise ValueError("Превышен кредитный лимит")

        self.debt += amount
        self._balance += amount

    def repay_credit(self, amount: float) -> None:
        amount = validate_amount(amount)

        if not self.is_active:
            raise ValueError("Нельзя погасить кредит у неактивного счёта")

        if amount > self.debt:
            raise ValueError("Сумма погашения больше текущего долга")

        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")

        self.debt -= amount
        self._balance -= amount

    def calculate(self) -> float:
        return self._balance - self.debt

    def to_string(self) -> str:
        return (
            f"Кредитный счёт | "
            f"Владелец: {self.owner_name} | "
            f"Номер: {self.account_number} | "
            f"Доступно с учётом долга: {self.calculate():.2f} {self.currency}"
        )

    def compare_to(self, other: object) -> int:
        if not isinstance(other, Comparable):
            raise TypeError("Сравнивать можно только с объектом Comparable")

        if self.calculate() > other.calculate():
            return 1

        if self.calculate() < other.calculate():
            return -1

        return 0

    def __str__(self) -> str:
        return (
            f"[Credit] {super().__str__()} | "
            f"лимит: {self.credit_limit} | долг: {self.debt}"
        )