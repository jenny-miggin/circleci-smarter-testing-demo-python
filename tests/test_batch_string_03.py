from myproj.lib.string_utils import truncate, words, is_palindrome, capitalize


def test_truncate_1(): assert truncate("abcdefgh", 6) == "abc..."
def test_words_1(): assert words("") == []
def test_is_palindrome_1(): assert is_palindrome("racecar") is True
def test_is_palindrome_2(): assert is_palindrome("no") is False
def test_capitalize_1(): assert capitalize("foo") == "Foo"
def test_truncate_2(): assert truncate("x", 1) == "x"
def test_words_2(): assert words("a  b  c") == ["a", "b", "c"]
def test_is_palindrome_3(): assert is_palindrome("mom") is True
def test_capitalize_2(): assert capitalize("bar") == "Bar"
def test_truncate_3(): assert truncate("noclip", 20) == "noclip"
