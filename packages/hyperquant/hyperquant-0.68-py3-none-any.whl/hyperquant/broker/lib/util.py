from decimal import ROUND_HALF_UP, Decimal


def fmt_value(price: float, tick: float) -> str:
    tick_dec = Decimal(str(tick))
    price_dec = Decimal(str(price))
    return str(
        (price_dec / tick_dec).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * tick_dec
    )
