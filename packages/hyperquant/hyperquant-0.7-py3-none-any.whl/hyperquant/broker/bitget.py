from __future__ import annotations

import asyncio
import itertools
import logging
import time
from typing import Any, Iterable, Literal

import pybotters

from .models.bitget import BitgetDataStore
from .lib.util import fmt_value

logger = logging.getLogger(__name__)



class Bitget:
    """Bitget public market-data client (REST + WS)."""

    def __init__(
        self,
        client: pybotters.Client,
        *,
        rest_api: str | None = None,
        ws_url: str | None = None,
    ) -> None:
        self.client = client
        self.store = BitgetDataStore()

        self.rest_api = rest_api or "https://api.bitget.com"
        self.ws_url = ws_url or "wss://ws.bitget.com/v2/ws/public"
        self.ws_url_private = ws_url or "wss://ws.bitget.com/v2/ws/private"

        self._ws_app = None


    async def __aenter__(self) -> "Bitget":
        await self.update("detail")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        pass

    async def update(
        self,
        update_type: Literal["detail", 'all'] = "all",
    ) -> None:
        fet = []
        if update_type in ("detail", "all"):
            fet.append(
                self.client.get(
                    f"{self.rest_api}/api/v2/mix/market/contracts?productType=usdt-futures",
                )
            )

        await self.store.initialize(*fet)

    async def place_order(
        self,
        symbol: str,
        *,
        direction: Literal["buy", "sell", "0", "1"],
        volume: float,
        price: float | None = None,
        order_type: Literal["market", "limit_ioc", "limit_gtc"] = "market",
        offset_flag: Literal["open", "close", "0", "1"] = "open",
        exchange_id: str = "Exchange",
        product_group: str = "SwapU",
        order_proportion: str = "0.0000",
        client_order_id: str | None = None,
    ) -> dict[str, Any]:
       pass

    async def cancel_order(
        self,
        order_sys_id: str,
        *,
        action_flag: str | int = "1",
    ) -> dict[str, Any]:
        pass


    async def sub_orderbook(self, symbols: list[str], channel: str = 'books1') -> None:
        """订阅指定交易对的订单簿（遵循 LBank 协议）。
        """

        submsg = {
            "op": "subscribe",
            "args": []
        }
        for symbol in symbols:
            submsg["args"].append(
                {"instType": "SPOT", "channel": channel, "instId": symbol}
            )

        self.client.ws_connect(
            self.ws_url,
            send_json=submsg,
            hdlr_json=self.store.onmessage
        )