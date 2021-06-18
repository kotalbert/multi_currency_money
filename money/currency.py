from __future__ import annotations

from typing import Any
from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount: float):
        self._amount = amount

    @staticmethod
    def dollar(amount: float) -> Money:
        return Dollar(amount)

    @staticmethod
    def franc(amount: float) -> Money:
        return Franc(amount)

    def times(self, times: float) -> Money:
        return self.__class__((self._amount * times))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._amount == other._amount


class Dollar(Money):
    pass


class Franc(Money):
    pass
