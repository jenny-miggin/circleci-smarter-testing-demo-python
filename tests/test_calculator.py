import pytest
from myproj.services.calculator import evaluate


def test_evaluate_add():
    assert evaluate("1 + 2") == 3


def test_evaluate_subtract():
    assert evaluate("10 - 3") == 7


def test_evaluate_multiply():
    assert evaluate("4 * 5") == 20


def test_evaluate_divide():
    assert evaluate("20 / 4") == 5


def test_evaluate_invalid():
    with pytest.raises(ValueError):
        evaluate("1 +")
    with pytest.raises(ValueError):
        evaluate("1 ? 2")
