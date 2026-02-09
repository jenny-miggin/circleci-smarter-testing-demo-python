from myproj.services.calculator import evaluate


def test_1(): assert evaluate("3 * 4") == 12
def test_2(): assert evaluate("15 / 3") == 5
def test_3(): assert evaluate("5 + 5") == 10
def test_4(): assert evaluate("20 - 10") == 10
def test_5(): assert evaluate("2 * 10") == 20
def test_6(): assert evaluate("8 / 2") == 4
def test_7(): assert evaluate("1 + 2") == 3
def test_8(): assert evaluate("6 - 1") == 5
def test_9(): assert evaluate("7 * 7") == 49
def test_10(): assert evaluate("18 / 6") == 3
