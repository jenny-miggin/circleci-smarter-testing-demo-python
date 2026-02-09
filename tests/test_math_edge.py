import pytest
from myproj.lib.math import add, divide, clamp


def test_add_zeros():
    assert add(0, 0) == 0


def test_clamp_boundaries():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_divide_float_result():
    assert divide(1, 2) == 0.5
