import json
import logging
import os
import sys
import types
import importlib
import time


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

    client = EXIR(api_url=api_url, api_key=api_key, api_secret=api_secret, ws_url=ws_url)


    symbol = "btc-usdt"

    def on_message(message: str):
        try:
            payload = json.loads(message)
        except Exception:
            payload = message
        logging.info("WS message: %s", payload if isinstance(payload, dict) else str(payload)[:500])

    def on_error(error):
        logging.error("WS error: %s", error)

    def on_close(status_code, msg):
        logging.info("WS closed: code=%s msg=%s", status_code, msg)

    try:
        logging.info("Connecting WebSocket and subscribing to orderbook:%s", symbol)
        client.connect(events=[f"order"], on_message=on_message, on_error=on_error, on_close=on_close)
        logging.info("Listening for orderbook updates for 10 seconds...")
        time.sleep(10)
    except Exception as exc:
        logging.exception("WebSocket error: %s", exc)
    finally:
        try:
            client.disconnect()
        except Exception:
            pass


if __name__ == "__main__":
    main()


