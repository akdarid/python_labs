from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SRC_DIR = PROJECT_ROOT / "src"

for path in (
    PROJECT_ROOT,
    SRC_DIR,
    SRC_DIR / "lab03",
    SRC_DIR / "laba_03",
):
    if path.exists() and str(path) not in sys.path:
        sys.path.insert(0, str(path))


from app import BankConsoleApp
from cli import BankCLI
from exceptions import StorageError


def main() -> None:
    """Запустить консольное приложение лабораторной работы №7."""
    data_file = Path(__file__).resolve().parent / "accounts.json"

    try:
        app = BankConsoleApp(data_file)
    except StorageError as error:
        print(f"Ошибка загрузки данных: {error}")
        print("Приложение будет запущено с пустой коллекцией.")
        app = BankConsoleApp(data_file, autoload=False)

    cli = BankCLI(app)
    cli.run()


if __name__ == "__main__":
    main()