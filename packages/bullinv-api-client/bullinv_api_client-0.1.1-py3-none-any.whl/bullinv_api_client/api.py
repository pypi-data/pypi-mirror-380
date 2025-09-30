from __future__ import annotations

import asyncio
import json
from typing import AsyncIterator, Iterable, Literal, Union

from .models import Aggregate, Indicators
from .ws_client import Subscription, WSClientConfig, WebSocketStream


Endpoint = Literal["aggregates", "indicators"]


def _make_url(base_ws_url: str, endpoint: Endpoint) -> str:
    base = base_ws_url.rstrip("/")
    return f"{base}/{endpoint}"


async def stream(
    base_ws_url: str,
    endpoint: Endpoint,
    subscriptions: Union[str, Iterable[Subscription]] | None = None,
    *,
    api_key: str | None = None,
    max_queue_size: int = 1000,
    drops_before_close: int = 100,
) -> AsyncIterator[dict]:
    config = WSClientConfig(
        url=_make_url(base_ws_url, endpoint),
        api_key=api_key,
        max_queue_size=max_queue_size,
        drops_before_close=drops_before_close,
    )
    stream = WebSocketStream(config)
    await stream.connect()
    try:
        if subscriptions:
            subs_list: list[Subscription]
            if isinstance(subscriptions, str):
                # Expect comma-separated topics like "15m.*,1m.AAPL"
                parts = [p.strip() for p in subscriptions.split(",") if p.strip()]
                subs_list = [Subscription(*p.split(".", 1)) for p in parts]
            else:
                subs_list = list(subscriptions)
            await stream.subscribe(subs_list)
        async for raw in stream.messages():
            yield json.loads(raw.decode())
    finally:
        await stream.close()


async def stream_aggregates(
    base_ws_url: str = "wss://quote-ws.bullinv.tech",
    subscriptions: Iterable[Subscription] | None = None,
    api_key: str | None = None,
    **kwargs,
) -> AsyncIterator[Aggregate]:
    async for obj in stream(base_ws_url, "aggregates", subscriptions, api_key=api_key, **kwargs):
        yield Aggregate.from_dict(obj)


async def stream_indicators(
    base_ws_url: str = "wss://quote-ws.bullinv.tech",
    subscriptions: Iterable[Subscription] | None = None,
    api_key: str | None = None,
    **kwargs,
) -> AsyncIterator[Indicators]:
    async for obj in stream(base_ws_url, "indicators", subscriptions, api_key=api_key, **kwargs):
        yield Indicators.from_dict(obj)


