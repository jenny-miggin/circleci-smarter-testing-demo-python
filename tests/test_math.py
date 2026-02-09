import pytest
from myproj.lib.math import add, subtract, multiply, divide, clamp


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5
    with pytest.raises(ValueError, match="Division by zero"):
        divide(1, 0)


def test_clamp():
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10
