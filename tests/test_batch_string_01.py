from myproj.lib.string_utils import capitalize, reverse, truncate, words, is_palindrome


def test_capitalize_1(): assert capitalize("a") == "A"
def test_capitalize_2(): assert capitalize("hello") == "Hello"
def test_reverse_1(): assert reverse("ab") == "ba"
def test_reverse_2(): assert reverse("xyz") == "zyx"
def test_truncate_1(): assert truncate("hi", 10) == "hi"
def test_truncate_2(): assert truncate("hello world", 5) == "he..."
def test_words_1(): assert words("a b") == ["a", "b"]
def test_words_2(): assert words("x") == ["x"]
def test_is_palindrome_1(): assert is_palindrome("a") is True
def test_is_palindrome_2(): assert is_palindrome("ab") is False
