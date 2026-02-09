from myproj.lib.math import add, subtract, multiply, divide, clamp


def test_add_1(): assert add(0, 0) == 0
def test_add_2(): assert add(1, 1) == 2
def test_add_3(): assert add(10, 20) == 30
def test_add_4(): assert add(-1, 1) == 0
def test_add_5(): assert add(100, 200) == 300
def test_subtract_1(): assert subtract(5, 2) == 3
def test_subtract_2(): assert subtract(0, 0) == 0
def test_multiply_1(): assert multiply(2, 3) == 6
def test_divide_1(): assert divide(6, 2) == 3
def test_clamp_1(): assert clamp(5, 0, 10) == 5
