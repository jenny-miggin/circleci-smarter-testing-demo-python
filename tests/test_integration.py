from myproj.services.calculator import evaluate
from myproj.lib.math import add, multiply
from myproj.utils.slug import slugify


def test_calc_uses_math():
    assert evaluate("1 + 2") == add(1, 2)
    assert evaluate("3 * 4") == multiply(3, 4)


def test_slug_roundtrip():
    title = "Hello World"
    assert slugify(title) == "hello-world"
