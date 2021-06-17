from __future__ import annotations

from typing import Any


class Dollar:
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, times: float) -> Dollar:
        return Dollar(self._amount * times)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Dollar):
            return False
        return self.amount == other.amount
