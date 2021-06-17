from __future__ import annotations


class Dollar:
    def __init__(self, amount: float):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def times(self, times: float) -> Dollar:
        return Dollar(self._amount * times)
