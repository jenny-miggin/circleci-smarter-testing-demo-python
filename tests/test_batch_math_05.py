from myproj.lib.math import add, subtract, divide, clamp


def test_add_1(): assert add(50, 50) == 100
def test_subtract_1(): assert subtract(20, 5) == 15
def test_divide_1(): assert divide(8, 4) == 2
def test_clamp_1(): assert clamp(15, 10, 20) == 15
def test_add_2(): assert add(6, 6) == 12
def test_subtract_2(): assert subtract(7, 2) == 5
def test_divide_2(): assert divide(15, 5) == 3
def test_clamp_2(): assert clamp(9, 10, 20) == 10
def test_add_3(): assert add(8, 9) == 17
def test_clamp_3(): assert clamp(25, 10, 20) == 20
