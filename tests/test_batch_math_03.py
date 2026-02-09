from myproj.lib.math import add, divide, clamp


def test_add_1(): assert add(11, 22) == 33
def test_add_2(): assert add(99, 1) == 100
def test_divide_1(): assert divide(9, 3) == 3
def test_divide_2(): assert divide(100, 10) == 10
def test_clamp_1(): assert clamp(3, 1, 5) == 3
def test_clamp_2(): assert clamp(100, 0, 50) == 50
def test_clamp_3(): assert clamp(7, 0, 20) == 7
def test_add_3(): assert add(0, 42) == 42
def test_divide_3(): assert divide(1, 1) == 1
def test_clamp_4(): assert clamp(2, 2, 2) == 2
