from __future__ import annotations

from typing import Any


class Money:
    def __init__(self, amount: float):
        self._amount = amount

    def times(self, times: float) -> Money:
        return Dollar(self._amount * times)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Money):
            return False
        return self._amount == other._amount


class Dollar(Money):
    pass


class Franc(Money):
    pass
