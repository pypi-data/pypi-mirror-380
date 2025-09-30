from __future__ import annotations

import json
import time
from typing import Generic, Iterable, Iterator, Optional, TypeVar, Union
import logging

import websocket

from .ws_client import Subscription
from .parsers import parse_subscriptions, parse_aggregate, parse_indicators


T = TypeVar("T")

logger = logging.getLogger(__name__)

class SyncStream(Generic[T]):
    def __init__(
        self,
        endpoint: str,
        *,
        base_ws_url: str,
        api_key: Optional[str] = None,
        topics: Union[str, Iterable[Union[str, Subscription]]],
        max_queue_size: int = 1000,  # kept for API compatibility, unused here
        drops_before_close: int = 100,  # kept for API compatibility, unused here
    ) -> None:
        self._endpoint = endpoint
        self._url = base_ws_url.rstrip("/") + "/" + endpoint
        self._api_key = api_key
        # Normalize topics to params string
        if isinstance(topics, str):
            subs = list(parse_subscriptions(topics))
        else:
            tmp: list[Subscription] = []
            for t in topics:
                if isinstance(t, Subscription):
                    tmp.append(t)
                else:
                    tmp.append(Subscription(*t.split(".", 1)))
            subs = tmp
        self._params = ",".join(s.to_param() for s in subs)
        self._ws: Optional[websocket.WebSocket] = None
        self._closed = False

    def _ensure_connected(self) -> None:
        if self._ws is not None:
            return
        backoff = 0.5
        while not self._closed:
            try:
                self._ws = websocket.create_connection(self._url, timeout=10)
                # First send auth frame if provided
                if self._api_key:
                    self._ws.send(json.dumps({"auth": self._api_key}))
                subscribe = json.dumps({"action": "subscribe", "params": self._params})
                self._ws.send(subscribe)
                return
            except Exception:
                self._ws = None
                time.sleep(backoff)
                backoff = min(30.0, backoff * 2)

    def __iter__(self) -> Iterator[T]:
        return self

    def __next__(self) -> T:
        if self._closed:
            raise StopIteration
        self._ensure_connected()
        if self._ws is None:
            raise StopIteration
        while not self._closed:
            try:
                frame = self._ws.recv()
                if frame is None:
                    # server closed
                    self._ws.close()
                    self._ws = None
                    self._ensure_connected()
                    continue
                # If server indicates unauthorized, close and stop
                try:
                    obj = json.loads(frame)
                    if isinstance(obj, dict) and obj.get("type") == "error" and obj.get("message") == "unauthorized":
                        logger.error("Unauthorized error received; closing connection. Check your API key.")
                        try:
                            self._ws.close()
                        finally:
                            self._ws = None
                        self._closed = True
                        raise StopIteration
                except Exception:
                    pass
                if self._endpoint == "aggregates":
                    return parse_aggregate(frame)
                return parse_indicators(frame)
            except Exception:
                # reconnect
                try:
                    if self._ws is not None:
                        self._ws.close()
                except Exception:
                    pass
                self._ws = None
                self._ensure_connected()
        raise StopIteration

    def close(self) -> None:
        self._closed = True
        try:
            if self._ws is not None:
                self._ws.close()
        finally:
            self._ws = None


class BullInv:
    def __init__(self, base_ws_url: str = "wss://quote-ws.bullinv.tech", api_key: Optional[str] = None) -> None:
        self._base_ws_url = base_ws_url
        self._api_key = api_key

    def aggregates(
        self,
        topics: Union[str, Iterable[Union[str, Subscription]]],
        *,
        max_queue_size: int = 1000,
        drops_before_close: int = 100,
    ) -> SyncStream:
        return SyncStream(
            "aggregates",
            base_ws_url=self._base_ws_url,
            api_key=self._api_key,
            topics=topics,
            max_queue_size=max_queue_size,
            drops_before_close=drops_before_close,
        )

    def indicators(
        self,
        topics: Union[str, Iterable[Union[str, Subscription]]],
        *,
        max_queue_size: int = 1000,
        drops_before_close: int = 100,
    ) -> SyncStream:
        return SyncStream(
            "indicators",
            base_ws_url=self._base_ws_url,
            api_key=self._api_key,
            topics=topics,
            max_queue_size=max_queue_size,
            drops_before_close=drops_before_close,
        )


