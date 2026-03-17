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
        if not isinstance(owner_name, str):
            raise TypeError("owner_name должен быть строкой")
        if not owner_name.strip():
            raise ValueError("owner_name не должен быть пустым")

        if not isinstance(account_number, str):
            raise TypeError("account_number должен быть строкой")
        if not account_number.strip():
            raise ValueError("account_number не должен быть пустым")

        if not isinstance(balance, (int, float)):
            raise TypeError("balance должен быть числом")
        if balance < 0:
            raise ValueError("balance не может быть отрицательным")

        if not isinstance(currency, str):
            raise TypeError("currency должен быть строкой")
        if not currency.strip():
            raise ValueError("currency не должна быть пустой")

        if not isinstance(is_active, bool):
            raise TypeError("is_active должен быть логическим значением")

        self._owner_name: str = owner_name.strip() ## внутри объекта будет храниться уже нормальное имя
        self._account_number: str = account_number.strip()
        self._balance: float = float(balance)
        self._currency: str = currency.strip().upper()
        self._is_active: bool = is_active

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

    def deposit(self, amount: float) -> None:
        if not self._is_active:
            raise ValueError("Нельзя пополнить неактивный счёт")

        if not isinstance(amount, (int, float)):
            raise TypeError("amount должен быть числом")
        if amount <= 0:
            raise ValueError("amount должен быть больше 0")

        self._balance += float(amount)

    def withdraw(self, amount: float) -> None:
        if not self._is_active:
            raise ValueError("Нельзя снимать деньги с неактивного счёта")

        if not isinstance(amount, (int, float)):
            raise TypeError("amount должен быть числом")
        if amount <= 0:
            raise ValueError("amount должен быть больше 0")
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")

        self._balance -= float(amount)

    def can_withdraw(self, amount: float) -> bool:
        if not isinstance(amount, (int, float)):
            return False
        if amount <= 0:
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