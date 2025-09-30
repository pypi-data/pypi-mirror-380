from __future__ import annotations

import threading
import time
from enum import Enum
from queue import Queue, Empty, Full
from typing import Callable, Iterable, List, Optional, Set

from .sync_client import BullInv


class Feed(Enum):
    Delayed = "delayed"
    RealTime = "realtime"


class Market(Enum):
    Stocks = "stocks"


class DataType(Enum):
    Aggregates = "aggregates"
    Indicators = "indicators"

# Backward-compatible alias
StreamKind = DataType


class WebSocketClient:
    def __init__(
        self,
        api_key: Optional[str] = None,
        *,
        url: str = "wss://quote-ws.bullinv.tech",
        feed: Optional[Feed] = None,
        market: Optional[Market] = None,
        batch_interval_seconds: float = 0.25,
        max_queue_size: int = 1000,
    ) -> None:
        self._url = url
        self._api_key = api_key
        self._feed = feed
        self._market = market
        self._batch_interval = batch_interval_seconds
        self._max_queue_size = max_queue_size

        self._agg_topics: Set[str] = set()
        self._ind_topics: Set[str] = set()

        self._queue: "Queue[object]" = Queue(maxsize=max_queue_size)
        self._stop = threading.Event()
        self._threads: list[threading.Thread] = []

    def subscribe(
        self,
        *topics,
        datatype: DataType | None = None,
        kind: DataType | None = None,
        streamtype: DataType | None = None,
        datakind: DataType | None = None,
        datalind: DataType | None = None,
    ) -> None:
        # Allow second positional enum argument
        enum_in_args = next((t for t in topics if isinstance(t, DataType)), None)
        dt = datatype or kind or streamtype or datakind or datalind or enum_in_args
        if dt is None:
            raise ValueError("Missing data type. Provide datatype=DataType.Aggregates/Indicators or as second positional argument.")
        # Normalize topics (strings only)
        topic_strs = [t.strip() for t in topics if isinstance(t, str) and t and t.strip()]
        if dt == DataType.Aggregates:
            self._agg_topics.update(topic_strs)
        elif dt == DataType.Indicators:
            self._ind_topics.update(topic_strs)
        else:
            raise ValueError("Unsupported data type")

    def _start_worker(self, datatype: DataType, topics: Iterable[str]) -> None:
        client = BullInv(self._url, api_key=self._api_key)
        if datatype == DataType.Aggregates:
            stream = client.aggregates(topics)
        else:
            stream = client.indicators(topics)

        def run() -> None:
            try:
                for item in stream:
                    try:
                        self._queue.put(item, timeout=0.1)
                    except Full:
                        # Drop oldest
                        try:
                            _ = self._queue.get_nowait()
                        except Empty:
                            pass
                        try:
                            self._queue.put(item, timeout=0.1)
                        except Full:
                            pass
                    if self._stop.is_set():
                        break
            finally:
                stream.close()

        th = threading.Thread(target=run, daemon=True)
        th.start()
        self._threads.append(th)

    def run(self, handler: Callable[[List[object]], None]) -> None:
        if not self._agg_topics and not self._ind_topics:
            raise ValueError("No subscriptions. Call subscribe(..., kind=...) before run().")

        if self._agg_topics:
            self._start_worker(DataType.Aggregates, list(self._agg_topics))
        if self._ind_topics:
            self._start_worker(DataType.Indicators, list(self._ind_topics))

        try:
            batch: list[object] = []
            last_flush = time.time()
            while not self._stop.is_set():
                timeout = max(0.0, self._batch_interval - (time.time() - last_flush))
                try:
                    item = self._queue.get(timeout=timeout if timeout > 0 else 0.01)
                    batch.append(item)
                except Empty:
                    pass

                now = time.time()
                if batch and (now - last_flush >= self._batch_interval):
                    handler(batch)
                    batch = []
                    last_flush = now
        finally:
            self.close()

    def close(self) -> None:
        if not self._stop.is_set():
            self._stop.set()
        for th in self._threads:
            th.join(timeout=1.0)
        self._threads.clear()


