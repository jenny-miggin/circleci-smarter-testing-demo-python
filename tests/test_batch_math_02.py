from myproj.lib.math import add, subtract, multiply, clamp


def test_add_1(): assert add(3, 4) == 7
def test_add_2(): assert add(7, 8) == 15
def test_add_3(): assert add(-5, 5) == 0
def test_subtract_1(): assert subtract(10, 4) == 6
def test_subtract_2(): assert subtract(1, 1) == 0
def test_multiply_1(): assert multiply(5, 5) == 25
def test_multiply_2(): assert multiply(0, 99) == 0
def test_clamp_1(): assert clamp(0, 0, 5) == 0
def test_clamp_2(): assert clamp(10, 0, 10) == 10
def test_clamp_3(): assert clamp(-1, 0, 10) == 0
