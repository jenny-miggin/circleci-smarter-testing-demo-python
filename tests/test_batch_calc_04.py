from myproj.services.calculator import evaluate


def test_1(): assert evaluate("2 + 8") == 10
def test_2(): assert evaluate("15 - 7") == 8
def test_3(): assert evaluate("4 * 4") == 16
def test_4(): assert evaluate("25 / 5") == 5
def test_5(): assert evaluate("6 + 6") == 12
def test_6(): assert evaluate("30 - 20") == 10
def test_7(): assert evaluate("8 * 2") == 16
def test_8(): assert evaluate("36 / 6") == 6
def test_9(): assert evaluate("0 + 0") == 0
def test_10(): assert evaluate("100 - 50") == 50
