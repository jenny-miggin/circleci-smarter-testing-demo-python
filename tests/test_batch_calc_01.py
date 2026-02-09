from myproj.services.calculator import evaluate


def test_1(): assert evaluate("1 + 1") == 2
def test_2(): assert evaluate("2 + 3") == 5
def test_3(): assert evaluate("10 - 3") == 7
def test_4(): assert evaluate("4 * 5") == 20
def test_5(): assert evaluate("20 / 4") == 5
def test_6(): assert evaluate("0 + 0") == 0
def test_7(): assert evaluate("9 - 4") == 5
def test_8(): assert evaluate("6 * 6") == 36
def test_9(): assert evaluate("100 / 10") == 10
def test_10(): assert evaluate("7 + 8") == 15
