import json
import logging
import os
import sys
import types
import importlib


def _prepare_local_package():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    package_name = "exir"

    if package_name not in sys.modules:
        pkg = types.ModuleType(package_name)
        pkg.__path__ = [repo_root]
        sys.modules[package_name] = pkg


def main():
    _prepare_local_package()

    EXIR = importlib.import_module("exir.index").EXIR  # type: ignore[attr-defined]

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    # Initialize with API credentials (replace with yours or env vars)
    api_key = os.getenv("EXIR_API_KEY", "<your-api-key>")
    api_secret = os.getenv("EXIR_API_SECRET", "<your-api-secret>")

    client = EXIR(api_url=api_url, api_key=api_key, api_secret=api_secret)

    try:
        user = client.get_user()
        logging.info("User response:\n%s", json.dumps(user, indent=2))
    except Exception as exc:
        logging.exception("Failed to fetch user: %s", exc)

    try:
        balance = client.get_balance()
        logging.info("Balance response:\n%s", json.dumps(balance, indent=2))
    except Exception as exc:
        logging.exception("Failed to fetch balance: %s", exc)


if __name__ == "__main__":
    main()


