from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Money:
    def __init__(self, amount: float, currency: str):
        self._amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount: float) -> Money:
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: float) -> Money:
        return Money(amount, 'CHF')

    def times(self, times: float) -> Money:
        return Money(self._amount * times, self._currency)

    @property
    def currency(self) -> str:
        return self._currency

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return (self._amount == other._amount) & (self._currency == other._currency)
