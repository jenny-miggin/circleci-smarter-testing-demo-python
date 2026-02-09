from myproj.lib.math import add, subtract, multiply


def test_add_1(): assert add(15, 25) == 40
def test_add_2(): assert add(200, 300) == 500
def test_subtract_1(): assert subtract(8, 3) == 5
def test_subtract_2(): assert subtract(100, 50) == 50
def test_multiply_1(): assert multiply(6, 7) == 42
def test_multiply_2(): assert multiply(10, 10) == 100
def test_add_3(): assert add(7, 7) == 14
def test_subtract_3(): assert subtract(9, 9) == 0
def test_multiply_3(): assert multiply(1, 100) == 100
def test_add_4(): assert add(12, 34) == 46
