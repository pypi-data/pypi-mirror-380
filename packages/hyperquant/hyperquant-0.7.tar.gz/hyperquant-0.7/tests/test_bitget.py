import pybotters
from hyperquant.broker.models.bitget import BitgetDataStore


async def test_update():
    async with pybotters.Client() as client:
        store = BitgetDataStore()
        # await store.initialize(
        #     client.get("https://api.bitget.com/api/v2/mix/market/contracts?productType=usdt-futures")
        # )
        # print(store.detail.find())
        await store.initialize(
            client.get(
                "https://api.bitget.com/api/v2/mix/market/tickers?productType=usdt-futures"
            )
        )
        print(store.ticker.find({"symbol": "BTCUSDT"}))


async def subscribe_book():

    async with pybotters.Client() as client:
        store = BitgetDataStore()
        client.ws_connect(
            "wss://ws.bitget.com/v2/ws/public",
            send_json={
                "op": "subscribe",
                "args": [
                    {"instType": "SPOT", "channel": "books1", "instId": "BTCUSDT"}
                ]
            },
            hdlr_json=store.onmessage
        )

        while True:
            await asyncio.sleep(1)
            print(store.book.find())

from hyperquant.broker.bitget import Bitget
async def test_broker_update():

    async with pybotters.Client() as client:
        bg = Bitget(client)
        store = BitgetDataStore()
        await bg.update('all')
        print(bg.store.detail.find())

async def test_broker_sub_orderbook():
    async with pybotters.Client() as client:
        bg = Bitget(client)
        await bg.sub_orderbook(['BTCUSDT', 'ETHUSDT'])
        while True:
            await asyncio.sleep(1)
            print(bg.store.book.find())

if __name__ == "__main__":
    import asyncio

    asyncio.run(test_broker_sub_orderbook())
