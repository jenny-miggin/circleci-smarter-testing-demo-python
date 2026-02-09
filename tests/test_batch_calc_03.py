from myproj.services.calculator import evaluate


def test_1(): assert evaluate("0 + 5") == 5
def test_2(): assert evaluate("10 - 10") == 0
def test_3(): assert evaluate("3 * 3") == 9
def test_4(): assert evaluate("12 / 4") == 3
def test_5(): assert evaluate("11 + 22") == 33
def test_6(): assert evaluate("50 - 25") == 25
def test_7(): assert evaluate("5 * 5") == 25
def test_8(): assert evaluate("14 / 7") == 2
def test_9(): assert evaluate("9 + 1") == 10
def test_10(): assert evaluate("8 - 3") == 5
