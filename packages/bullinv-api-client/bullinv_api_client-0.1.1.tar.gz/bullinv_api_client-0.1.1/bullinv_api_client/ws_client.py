from __future__ import annotations

import asyncio
import json
import logging
import random
from dataclasses import dataclass
from typing import AsyncIterator, Dict, Optional, Set

import websockets


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Subscription:
    timespan: str
    ticker: str

    def to_param(self) -> str:
        return f"{self.timespan}.{self.ticker}"


@dataclass
class WSClientConfig:
    url: str
    api_key: Optional[str] = None
    connect_timeout_seconds: float = 10.0
    heartbeat_interval_seconds: float = 20.0
    max_queue_size: int = 1000
    drops_before_close: int = 100
    max_backoff_seconds: float = 30.0
    initial_backoff_seconds: float = 0.5


class WebSocketStream:
    def __init__(self, config: WSClientConfig) -> None:
        self._config = config
        self._ws: Optional[websockets.WebSocketClientProtocol] = None
        self._recv_task: Optional[asyncio.Task[None]] = None
        self._queue: "asyncio.Queue[bytes]" = asyncio.Queue(maxsize=config.max_queue_size)
        self._drops: int = 0
        self._closed = asyncio.Event()
        self._want_close = False
        self._subscriptions: Set[Subscription] = set()

    async def __aenter__(self) -> "WebSocketStream":
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    async def connect(self) -> None:
        if self._ws is not None:
            return
        await self._dial_and_start()

    async def close(self) -> None:
        self._want_close = True
        if self._recv_task:
            self._recv_task.cancel()
            try:
                await self._recv_task
            except asyncio.CancelledError:
                pass
        if self._ws is not None:
            try:
                await self._ws.close()
            finally:
                self._ws = None
        self._closed.set()

    async def subscribe(self, subs: Set[Subscription] | list[Subscription] | Subscription) -> None:
        items = self._normalize_subs(subs)
        new_items = [s for s in items if s not in self._subscriptions]
        if not new_items:
            return
        await self._send_control("subscribe", new_items)
        self._subscriptions.update(new_items)

    async def unsubscribe(self, subs: Set[Subscription] | list[Subscription] | Subscription) -> None:
        items = self._normalize_subs(subs)
        to_remove = [s for s in items if s in self._subscriptions]
        if not to_remove:
            return
        await self._send_control("unsubscribe", to_remove)
        for s in to_remove:
            self._subscriptions.discard(s)

    def _normalize_subs(self, subs: Set[Subscription] | list[Subscription] | Subscription) -> list[Subscription]:
        if isinstance(subs, Subscription):
            return [subs]
        return list(subs)

    async def messages(self) -> AsyncIterator[bytes]:
        while True:
            if self._want_close and self._queue.empty():
                break
            try:
                msg = await self._queue.get()
            except asyncio.CancelledError:
                break
            yield msg

    async def _dial_and_start(self) -> None:
        backoff = self._config.initial_backoff_seconds
        while True:
            try:
                logger.info("Connecting to %s", self._config.url)
                self._ws = await asyncio.wait_for(
                    websockets.connect(self._config.url, max_queue=None, ping_interval=None),
                    timeout=self._config.connect_timeout_seconds,
                )
                # Send initial auth frame if configured
                if self._config.api_key:
                    await self._send_text(json.dumps({"auth": self._config.api_key}))
                # Resubscribe
                if self._subscriptions:
                    await self._send_control("subscribe", list(self._subscriptions))
                # Start receiver
                self._recv_task = asyncio.create_task(self._recv_loop())
                return
            except Exception as e:
                if self._want_close:
                    raise
                logger.warning("Connect failed: %s", e)
                await asyncio.sleep(backoff + random.uniform(0, backoff / 4))
                backoff = min(self._config.max_backoff_seconds, backoff * 2)

    async def _recv_loop(self) -> None:
        assert self._ws is not None
        try:
            async for raw in self._ws:
                data: bytes
                if isinstance(raw, str):
                    # Inspect for unauthorized error and close without reconnecting
                    try:
                        obj = json.loads(raw)
                        if isinstance(obj, dict) and obj.get("type") == "error" and obj.get("message") == "unauthorized":
                            logger.error("Unauthorized error received; closing connection. Check your API key.")
                            self._want_close = True
                            await self.close()
                            return
                    except Exception:
                        pass
                    data = raw.encode()
                else:
                    data = raw
                if self._queue.full():
                    try:
                        _ = self._queue.get_nowait()
                        self._drops += 1
                        if self._drops >= self._config.drops_before_close:
                            logger.error("Too many drops (%d), closing connection", self._drops)
                            await self.close()
                            return
                    except asyncio.QueueEmpty:
                        pass
                await self._queue.put(data)
        except Exception as e:
            if not self._want_close:
                logger.warning("Receive loop error: %s", e)
        finally:
            if not self._want_close:
                # attempt reconnect
                self._ws = None
                await self._dial_and_start()

    async def _send_control(self, action: str, items: list[Subscription]) -> None:
        params = ",".join(s.to_param() for s in items)
        payload = json.dumps({"action": action, "params": params})
        await self._send_text(payload)

    async def _send_text(self, text: str) -> None:
        if self._ws is None:
            await self._dial_and_start()
        assert self._ws is not None
        await self._ws.send(text)


