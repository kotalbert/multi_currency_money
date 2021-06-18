from money.currency import Money


def test_currency():
    assert 'USD' == Money.dollar(1).currency
    assert 'CHF' == Money.franc(1).currency
