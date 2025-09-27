from __future__ import annotations

import asyncio
import itertools
import logging
import time
from typing import Any, Iterable, Literal

import pybotters

from .models.lbank import LbankDataStore
from .lib.util import fmt_value

logger = logging.getLogger(__name__)

# https://ccapi.rerrkvifj.com 似乎是spot的api
# https://uuapi.rerrkvifj.com 似乎是合约的api


class Lbank:
    """LBank public market-data client (REST + WS)."""

    def __init__(
        self,
        client: pybotters.Client,
        *,
        front_api: str | None = None,
        rest_api: str | None = None,
        ws_url: str | None = None,
    ) -> None:
        self.client = client
        self.store = LbankDataStore()
        self.front_api = front_api or "https://uuapi.rerrkvifj.com"
        self.rest_api = rest_api or "https://api.lbkex.com"
        self.ws_url = ws_url or "wss://uuws.rerrkvifj.com/ws/v3"
        self._req_id = itertools.count(int(time.time() * 1000))
        self._ws_app = None
        self._rest_headers = {"source": "4", "versionflage": "true"}

    async def __aenter__(self) -> "Lbank":
        await self.update("detail")
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        pass

    async def update(
        self,
        update_type: Literal["detail", "balance", "position", "orders", "orders_finish", "all"] = "all",
        *,
        product_group: str = "SwapU",
        exchange_id: str = "Exchange",
        asset: str = "USDT",
        instrument_id: str | None = None,
        page_index: int = 1,
        page_size: int = 1000,
    ) -> None:
        """Refresh local caches via REST endpoints.

        Parameters mirror the documented REST API default arguments.
        """

        requests: list[Any] = []

        include_detail = update_type in {"detail", "all"}
        include_orders = update_type in {"orders", "all"}
        include_position = update_type in {"position", "all"}
        include_balance = update_type in {"balance", "all"}

        if update_type == "orders_finish":
            await self.update_finish_order(
                product_group=product_group,
                page_index=page_index,
                page_size=page_size,
            )
            return

        if include_detail:
            requests.append(
                self.client.post(
                    f"{self.front_api}/cfd/agg/v1/instrument",
                    json={"ProductGroup": product_group},
                    headers=self._rest_headers,
                )
            )

        if include_orders:
            requests.append(
                self.client.get(
                    f"{self.front_api}/cfd/query/v1.0/Order",
                    params={
                        "ProductGroup": product_group,
                        "ExchangeID": exchange_id,
                        "pageIndex": page_index,
                        "pageSize": page_size,
                    },
                    headers=self._rest_headers,
                )
            )
        
        if include_position:
            requests.append(
                self.client.get(
                    f"{self.front_api}/cfd/query/v1.0/Position",
                    params={
                        "ProductGroup": product_group,
                        "Valid": 1,
                        "pageIndex": page_index,
                        "pageSize": page_size,
                    },
                    headers=self._rest_headers,
                )
            )

        if include_balance:
            resolved_instrument = instrument_id or self._resolve_instrument()
            if not resolved_instrument:
                raise ValueError(
                    "instrument_id is required to query balance; call update('detail') first or provide instrument_id explicitly."
                )
            self.store.balance.set_asset(asset)
            requests.append(
                self.client.post(
                    f"{self.front_api}/cfd/agg/v1/sendQryAll",
                    json={
                        "productGroup": product_group,
                        "instrumentID": resolved_instrument,
                        "asset": asset,
                    },
                    headers=self._rest_headers,
                )
            )

        if not requests:
            raise ValueError(f"update_type err: {update_type}")

        await self.store.initialize(*requests)

    def _resolve_instrument(self) -> str | None:
        detail_entries = self.store.detail.find()
        if detail_entries:
            return detail_entries[0].get("symbol")
        return None

    def _get_detail_entry(self, symbol: str) -> dict[str, Any]:
        detail = self.store.detail.get({"symbol": symbol})
        if not detail:
            raise ValueError(f"Unknown LBank instrument: {symbol}")
        return detail

    @staticmethod
    def _format_with_step(value: float, step: Any) -> str:
        try:
            step_float = float(step)
        except (TypeError, ValueError):  # pragma: no cover - defensive guard
            step_float = 0.0

        if step_float <= 0:
            return str(value)

        return fmt_value(value, step_float)

    async def update_finish_order(
        self,
        *,
        product_group: str = "SwapU",
        page_index: int = 1,
        page_size: int = 200,
        start_time: int | None = None,
        end_time: int | None = None,
        instrument_id: str | None = None,
    ) -> None:
        """Fetch finished orders within the specified time window (default: last hour)."""

        now_ms = int(time.time() * 1000)
        if end_time is None:
            end_time = now_ms
        if start_time is None:
            start_time = end_time - 60 * 60 * 1000
        if start_time >= end_time:
            raise ValueError("start_time must be earlier than end_time")

        params: dict[str, Any] = {
            "ProductGroup": product_group,
            "pageIndex": page_index,
            "pageSize": page_size,
            "startTime": start_time,
            "endTime": end_time,
        }
        if instrument_id:
            params["InstrumentID"] = instrument_id

        await self.store.initialize(
            self.client.get(
                f"{self.front_api}/cfd/cff/v1/FinishOrder",
                params=params,
                headers=self._rest_headers,
            )
        )

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
        """Create an order using documented REST parameters."""

        direction_code = self._normalize_direction(direction)
        offset_code = self._normalize_offset(offset_flag)
        price_type_code, order_type_code = self._resolve_order_type(order_type)

        detail_entry = self._get_detail_entry(symbol)
        volume_str = self._format_with_step(volume, detail_entry.get("step_size"))
        price_str: str | None = None
        if price_type_code == "0":
            if price is None:
                raise ValueError("price is required for limit orders")
            price_str = self._format_with_step(price, detail_entry.get("tick_size"))

        payload: dict[str, Any] = {
            # "ProductGroup": product_group,
            "InstrumentID": symbol,
            "ExchangeID": exchange_id,
            "Direction": direction_code,
            "OffsetFlag": offset_code,
            "OrderPriceType": price_type_code,
            "OrderType": order_type_code,
            "Volume": volume_str,
            "orderProportion": order_proportion,
        }

        if price_type_code == "0":
            payload["Price"] = price_str
        elif price is not None:
            logger.warning("Price is ignored for market orders")

        # if client_order_id:
        #     payload["LocalID"] = client_order_id
        print(payload)
        res = await self.client.post(
            f"{self.front_api}/cfd/cff/v1/SendOrderInsert",
            json=payload,
            headers=self._rest_headers,
        )
        data = await res.json()
        return self._ensure_ok("place_order", data)

    async def cancel_order(
        self,
        order_sys_id: str,
        *,
        action_flag: str | int = "1",
    ) -> dict[str, Any]:
        """Cancel an order by OrderSysID."""

        payload = {"OrderSysID": order_sys_id, "ActionFlag": str(action_flag)}
        res = await self.client.post(
            f"{self.front_api}/cfd/action/v1.0/SendOrderAction",
            json=payload,
            headers=self._rest_headers,
        )
        data = await res.json()
        return self._ensure_ok("cancel_order", data)

    @staticmethod
    def _ensure_ok(operation: str, data: Any) -> dict[str, Any]:
        if not isinstance(data, dict) or data.get("code") != 200:
            raise RuntimeError(f"{operation} failed: {data}")
        return data.get("data") or {}

    @staticmethod
    def _normalize_direction(direction: str) -> str:
        mapping = {
            "buy": "0",
            "long": "0",
            "sell": "1",
            "short": "1",
        }
        return mapping.get(str(direction).lower(), str(direction))

    @staticmethod
    def _normalize_offset(offset: str) -> str:
        mapping = {
            "open": "0",
            "close": "1",
        }
        return mapping.get(str(offset).lower(), str(offset))

    @staticmethod
    def _resolve_order_type(order_type: str) -> tuple[str, str]:
        mapping = {
            "market": ("4", "1"),
            "limit_ioc": ("0", "1"),
            "limit_gtc": ("0", "0"),
        }
        try:
            return mapping[str(order_type).lower()]
        except KeyError as exc:  # pragma: no cover - guard
            raise ValueError(f"Unsupported order_type: {order_type}") from exc


    async def sub_orderbook(self, symbols: list[str], limit: int | None = None) -> None:
        """订阅指定交易对的订单簿（遵循 LBank 协议）。
        """

        async def sub(payload):
            wsapp = self.client.ws_connect(
                self.ws_url,
                hdlr_bytes=self.store.onmessage,
                send_json=payload,
            )
            await wsapp._event.wait()

        send_jsons = []
        y = 3000000001
        if limit:
            self.store.book.limit = limit

        for symbol in symbols:

            info = self.store.detail.get({"symbol": symbol})
            if not info:
                raise ValueError(f"Unknown LBank symbol: {symbol}")
            
            tick_size = info['tick_size']
            sub_i = symbol + "_" + str(tick_size) + "_25"
            send_jsons.append(
                {
                    "x": 3,
                    "y": str(y),
                    "a": {"i": sub_i},
                    "z": 1,
                }
            )

            self.store.register_book_channel(str(y), symbol)
            y += 1

        # Rate limit: max 5 subscriptions per second
        for i in range(0, len(send_jsons), 5):
            batch = send_jsons[i:i+5]
            await asyncio.gather(*(sub(send_json) for send_json in batch))
            if i + 5 < len(send_jsons):
                await asyncio.sleep(0.1)
