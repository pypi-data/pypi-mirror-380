from __future__ import annotations

import argparse
import asyncio
from typing import Iterable

from . import Subscription, stream_aggregates, stream_indicators


def parse_subs(arg: str) -> list[Subscription]:
    items = []
    for token in (arg or "").split(","):
        token = token.strip()
        if not token:
            continue
        if "." not in token:
            raise ValueError(f"Invalid subscription item: {token}")
        timespan, ticker = token.split(".", 1)
        items.append(Subscription(timespan, ticker))
    return items


async def run_indicators(url: str, subs: Iterable[Subscription], api_key: str | None) -> None:
    async for msg in stream_indicators(url, subs, api_key=api_key):
        print(msg)


async def run_aggregates(url: str, subs: Iterable[Subscription], api_key: str | None) -> None:
    async for msg in stream_aggregates(url, subs, api_key=api_key):
        print(msg)


def main() -> int:
    parser = argparse.ArgumentParser(description="BullInv WS SDK CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_ind = sub.add_parser("indicators", help="Stream indicators")
    p_ind.add_argument("--url", default="wss://quote-ws.bullinv.tech")
    p_ind.add_argument("--subs", default="15m.*")
    p_ind.add_argument("--api-key", dest="api_key", default=None)

    p_agg = sub.add_parser("aggregates", help="Stream aggregates")
    p_agg.add_argument("--url", default="wss://quote-ws.bullinv.tech")
    p_agg.add_argument("--subs", default="15m.*")
    p_agg.add_argument("--api-key", dest="api_key", default=None)

    args = parser.parse_args()
    subs = parse_subs(getattr(args, "subs", ""))

    if args.cmd == "indicators":
        asyncio.run(run_indicators(args.url, subs, args.api_key))
    elif args.cmd == "aggregates":
        asyncio.run(run_aggregates(args.url, subs, args.api_key))
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


