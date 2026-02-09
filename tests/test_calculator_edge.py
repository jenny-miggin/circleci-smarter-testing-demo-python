import pytest
from myproj.services.calculator import evaluate


def test_evaluate_whitespace():
    assert evaluate("  2   +   3  ") == 5


def test_evaluate_unknown_op():
    with pytest.raises(ValueError, match="Unknown operator"):
        evaluate("1 % 2")
