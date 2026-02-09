from myproj.lib.string_utils import capitalize, reverse, truncate, is_palindrome


def test_capitalize_1(): assert capitalize("demo") == "Demo"
def test_capitalize_2(): assert capitalize("x") == "X"
def test_reverse_1(): assert reverse("demo") == "omed"
def test_reverse_2(): assert reverse("xy") == "yx"
def test_truncate_1(): assert truncate("truncate me", 7) == "trun..."
def test_truncate_2(): assert truncate("short", 5) == "short"
def test_is_palindrome_1(): assert is_palindrome("level") is True
def test_is_palindrome_2(): assert is_palindrome("nope") is False
def test_capitalize_3(): assert capitalize("batch") == "Batch"
def test_reverse_3(): assert reverse("batch") == "hctab"
