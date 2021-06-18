from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Money(ABC):
    def __init__(self, amount: float, currency: str):
        self._amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount: float) -> Money:
        return Dollar(amount)

    @staticmethod
    def franc(amount: float) -> Money:
        return Franc(amount)

    @abstractmethod
    def times(self, times: float) -> Money:
        pass

    @property
    def currency(self) -> str:
        return self._currency

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._amount == other._amount


class Dollar(Money):
    def __init__(self, amount: float):
        super().__init__(amount, 'USD')

    def times(self, times: float) -> Money:
        return Dollar(self._amount * times)


class Franc(Money):
    def __init__(self, amount: float):
        super().__init__(amount, 'CHF')

    def times(self, times: float) -> Money:
        return Franc(self._amount * times)
