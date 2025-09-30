from __future__ import annotations

import asyncio
from typing import AsyncIterator, Iterable, Optional, Union

from .api import stream_aggregates, stream_indicators
from .ws_client import Subscription


class BullInvClient:
    """
    Polygon-like high-level client.

    Example:

        client = BullInvClient("ws://localhost:8080")
        async with client:
            async for bar in client.aggregates.subscribe(["15m.*", "1m.AAPL"]):
                print(bar)
    """

    def __init__(self, base_ws_url: str = "wss://quote-ws.bullinv.tech", api_key: Optional[str] = None) -> None:
        self._base_ws_url = base_ws_url
        self._api_key = api_key
        self.aggregates = _AggregatesAPI(self)
        self.indicators = _IndicatorsAPI(self)

    async def __aenter__(self) -> "BullInvClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        return None


def _parse_topic(topic: str) -> Subscription:
    # topic like "15m.*" or "1m.AAPL"
    if "." not in topic:
        raise ValueError(f"Invalid topic: {topic}")
    timespan, ticker = topic.split(".", 1)
    return Subscription(timespan, ticker)


class _AggregatesAPI:
    def __init__(self, client: BullInvClient) -> None:
        self._client = client

    async def subscribe(
        self,
        topics: Union[str, Iterable[str]],
        *,
        max_queue_size: int = 1000,
        drops_before_close: int = 100,
    ) -> AsyncIterator:
        if isinstance(topics, str):
            topics = topics.split(",")
        subs = [_parse_topic(t) for t in topics]
        async for agg in stream_aggregates(
            self._client._base_ws_url,
            subs,
            api_key=self._client._api_key,
            max_queue_size=max_queue_size,
            drops_before_close=drops_before_close,
        ):
            yield agg


class _IndicatorsAPI:
    def __init__(self, client: BullInvClient) -> None:
        self._client = client

    async def subscribe(
        self,
        topics: Union[str, Iterable[str]],
        *,
        max_queue_size: int = 1000,
        drops_before_close: int = 100,
    ) -> AsyncIterator:
        if isinstance(topics, str):
            topics = topics.split(",")
        subs = [_parse_topic(t) for t in topics]
        async for msg in stream_indicators(
            self._client._base_ws_url,
            subs,
            api_key=self._client._api_key,
            max_queue_size=max_queue_size,
            drops_before_close=drops_before_close,
        ):
            yield msg


