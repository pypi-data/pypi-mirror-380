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

    api_key = os.getenv("EXIR_API_KEY", "<your-api-key>")
    api_secret = os.getenv("EXIR_API_SECRET", "<your-api-secret>")

    client = EXIR(api_url=api_url, api_key=api_key, api_secret=api_secret)

    symbol = "btc-usdt"
    try:
        order = client.create_order(symbol=symbol, side="buy", size=0.001, type="limit", price=50000)
        logging.info("Create order response:\n%s", json.dumps(order, indent=2))
    except Exception as exc:
        logging.exception("Failed to create order: %s", exc)


if __name__ == "__main__":
    main()


