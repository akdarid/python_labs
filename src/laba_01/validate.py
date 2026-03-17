def validate_owner_name(owner_name: str) -> str:
    if not isinstance(owner_name, str):
        raise TypeError("owner_name должен быть строкой")

    owner_name = owner_name.strip()
    if not owner_name:
        raise ValueError("owner_name не должен быть пустым")

    return owner_name


def validate_account_number(account_number: str) -> str:
    if not isinstance(account_number, str):
        raise TypeError("account_number должен быть строкой")

    account_number = account_number.strip()
    if not account_number:
        raise ValueError("account_number не должен быть пустым")

    return account_number


def validate_balance(balance: float) -> float:
    if not isinstance(balance, (int, float)):
        raise TypeError("balance должен быть числом")

    if balance < 0:
        raise ValueError("balance не может быть отрицательным")

    return float(balance)


def validate_currency(currency: str) -> str:
    if not isinstance(currency, str):
        raise TypeError("currency должен быть строкой")

    currency = currency.strip().upper()
    if not currency:
        raise ValueError("currency не должна быть пустой")

    return currency


def validate_is_active(is_active: bool) -> bool:
    if not isinstance(is_active, bool):
        raise TypeError("is_active должен быть логическим значением")

    return is_active


def validate_amount(amount: float) -> float:
    if not isinstance(amount, (int, float)):
        raise TypeError("amount должен быть числом")

    if amount <= 0:
        raise ValueError("amount должен быть больше 0")

    return float(amount)