## EXIR Python Client - Examples

This repository contains a lightweight Python client in `index.py` and runnable examples under `example/` for:
- **Public**: Fetching market data (e.g., ticker)
- **Private**: Authenticated calls (user, balance, place orders)
- **WebSocket**: Streaming market data (orderbook)

### Requirements
- Python 3.8+
- Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

### Project layout
- `index.py`: EXIR client (public, private, and WebSocket helpers)
- `utils.py`: HTTP and auth utilities
- `example/public.py`: Public ticker example
- `example/balance.py`: Private user + balance example
- `example/order.py`: Private create order example
- `example/websocket.py`: WebSocket orderbook subscription example

---

## Public usage

Fetch the ticker for `btc-usdt`:

```bash
python3 example/public.py
```

Example:

```bash
python3 example/public.py
```

---

## Private usage (user, balance)

Set your api keys:
```bash
EXIR_API_KEY=<your-api-key> \
EXIR_API_SECRET=<your-api-secret> \
```

Notes:
- Ensure your key has the required permissions (e.g., trading, read balance).
- If IP whitelisting is enabled on the key, include your current IP.
- Your system clock must be accurate; auth uses expiring signatures.

---

## Private usage (create order)

Places a limit BUY order for 0.001 BTC at 50,000 USDT on `btc-usdt`:

If you receive `401 Unauthorized` when creating orders:
- Check key permissions and IP whitelist
- Ensure your system clock is in sync

---

## WebSocket usage (orderbook)

Subscribes to `orderbook:btc-usdt` and logs messages for ~10 seconds:

Notes:
- Public WS channels (e.g., `orderbook`, `trade`) do not require credentials, but the script will include them if provided.
- The client automatically reconnects by default.
