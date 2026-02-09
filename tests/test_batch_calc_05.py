from myproj.services.calculator import evaluate


def test_1(): assert evaluate("1 * 100") == 100
def test_2(): assert evaluate("40 / 8") == 5
def test_3(): assert evaluate("12 + 13") == 25
def test_4(): assert evaluate("99 - 9") == 90
def test_5(): assert evaluate("10 * 10") == 100
def test_6(): assert evaluate("21 / 3") == 7
def test_7(): assert evaluate("4 + 5") == 9
def test_8(): assert evaluate("17 - 8") == 9
def test_9(): assert evaluate("2 * 7") == 14
def test_10(): assert evaluate("48 / 6") == 8
