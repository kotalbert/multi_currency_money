from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Money(ABC):
    def __init__(self, amount: float):
        self._amount = amount

    @staticmethod
    def dollar(amount: float) -> Money:
        return Dollar(amount)

    @staticmethod
    def franc(amount: float) -> Money:
        return Franc(amount)

    @abstractmethod
    def times(self, times: float) -> Money:
        pass

    @abstractmethod
    def currency(self) -> str:
        pass

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self._amount == other._amount


class Dollar(Money):
    def currency(self) -> str:
        return 'USD'

    def times(self, times: float) -> Money:
        return Dollar(self._amount * times)


class Franc(Money):
    def currency(self) -> str:
        return 'CHF'

    def times(self, times: float) -> Money:
        return Franc(self._amount * times)
