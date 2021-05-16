from funcc import Calculator
import pytest


def test_check_sum():
    assert Calculator.add(2, 5) == 7


def test_check_different():
    assert Calculator.subtract(4, 4) == 0


def test_chekc_multiply():
    assert Calculator.multiply(3, 3) == 9


def test_check_division():
    assert Calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        Calculator.divide(4,0)
