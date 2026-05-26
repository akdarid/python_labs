from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Sequence


CURRENT_DIR = Path(__file__).resolve().parent
SRC_DIR = CURRENT_DIR.parent

for path in (
    SRC_DIR / "lab03",
    SRC_DIR / "laba_03",
):
    if path.exists() and str(path) not in sys.path:
        sys.path.insert(0, str(path))


from base import BankAccount
from models import CreditAccount, SavingsAccount
from exceptions import StorageError


def account_to_dict(account: BankAccount) -> dict[str, Any]:
    """Преобразовать объект счёта в словарь для сохранения в JSON."""
    base_data: dict[str, Any] = {
        "owner_name": account.owner_name,
        "account_number": account.account_number,
        "balance": account.balance,
        "currency": account.currency,
        "is_active": account.is_active,
    }

    if isinstance(account, SavingsAccount):
        base_data.update(
            {
                "type": "savings",
                "interest_rate": account.interest_rate,
                "bonus": account.bonus,
            }
        )
        return base_data

    if isinstance(account, CreditAccount):
        base_data.update(
            {
                "type": "credit",
                "credit_limit": account.credit_limit,
                "debt": account.debt,
            }
        )
        return base_data

    base_data["type"] = "bank"
    return base_data


def account_from_dict(data: dict[str, Any]) -> BankAccount:
    """Создать объект счёта из словаря, загруженного из JSON."""
    try:
        account_type = str(data["type"])

        owner_name = str(data["owner_name"])
        account_number = str(data["account_number"])
        balance = float(data["balance"])
        currency = str(data["currency"])
        is_active = bool(data.get("is_active", True))

        if account_type == "savings":
            return SavingsAccount(
                owner_name,
                account_number,
                balance,
                currency,
                float(data["interest_rate"]),
                float(data["bonus"]),
                is_active,
            )

        if account_type == "credit":
            return CreditAccount(
                owner_name,
                account_number,
                balance,
                currency,
                float(data["credit_limit"]),
                float(data["debt"]),
                is_active,
            )

        if account_type == "bank":
            return BankAccount(
                owner_name,
                account_number,
                balance,
                currency,
                is_active,
            )

        raise StorageError(f"Неизвестный тип счёта: {account_type}")

    except KeyError as error:
        raise StorageError(f"В JSON отсутствует поле: {error}") from error
    except (TypeError, ValueError) as error:
        raise StorageError(f"Некорректные данные счёта: {error}") from error


def save_accounts(accounts: Sequence[BankAccount], filepath: Path) -> None:
    """Сохранить коллекцию банковских счетов в JSON-файл."""
    try:
        filepath.parent.mkdir(parents=True, exist_ok=True)

        data = [account_to_dict(account) for account in accounts]

        with filepath.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except OSError as error:
        raise StorageError(f"Не удалось сохранить файл: {error}") from error


def load_accounts(filepath: Path) -> list[BankAccount]:
    """Загрузить банковские счета из JSON-файла."""
    if not filepath.exists():
        return []

    try:
        with filepath.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise StorageError("JSON-файл должен содержать список счетов")

        return [account_from_dict(item) for item in data]

    except json.JSONDecodeError as error:
        raise StorageError(f"Ошибка чтения JSON: {error}") from error
    except OSError as error:
        raise StorageError(f"Не удалось открыть файл: {error}") from error