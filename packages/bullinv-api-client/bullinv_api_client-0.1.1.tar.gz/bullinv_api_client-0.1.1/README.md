BullInv API Client (WebSocket SDK)

Python SDK to consume aggregate market data and indicators from the SDK Data Streamer WebSocket service.

Quick start (uv)

```bash
uv venv
uv pip install -e .
```

Usage (polygon-style client)

```python
import asyncio
from bullinv_api_client import BullInvClient


async def main():
    async with BullInvClient(api_key="live_pk_9f3a2e1c4b7d") as client:
        async for ind in client.indicators.subscribe(["15m.*", "1m.AAPL"]):
            print(ind)


if __name__ == "__main__":
    asyncio.run(main())
```

CLI example (uv)

```bash
uv run bullinv-ws indicators --subs "15m.*,1m.AAPL" --api-key live_pk_9f3a2e1c4b7d
uv run bullinv-ws aggregates --subs "1m.MSFT" --api-key live_pk_9f3a2e1c4b7d
```


