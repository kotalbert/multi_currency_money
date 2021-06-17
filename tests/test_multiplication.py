def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert five.ammount == 10
