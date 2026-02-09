from myproj.lib.string_utils import capitalize, reverse, truncate, words, is_palindrome


def test_capitalize():
    assert capitalize("hello") == "Hello"


def test_reverse():
    assert reverse("abc") == "cba"


def test_truncate():
    assert truncate("hello world", 8) == "hello..."


def test_words():
    assert words("  a  b  c  ") == ["a", "b", "c"]


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
