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

    # Import from the local package so relative imports inside index.py work
    EXIR = importlib.import_module("exir.index").EXIR  # type: ignore[attr-defined]

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    client = EXIR()

    symbol = "btc-irt"
    logging.info("Requesting ticker for symbol=%s", symbol)
    try:
        ticker = client.get_ticker(symbol=symbol)
        logging.info("Ticker response:\n%s", json.dumps(ticker, indent=2))
    except Exception as exc:
        logging.exception("Failed to fetch ticker: %s", exc)

if __name__ == "__main__":
    main()


