from myproj.lib.string_utils import capitalize, truncate, is_palindrome


def test_capitalize_empty():
    assert capitalize("") == ""


def test_truncate_short_string():
    assert truncate("hi", 10) == "hi"


def test_is_palindrome_ignores_non_alnum():
    assert is_palindrome("A man a plan a canal Panama") is True
