from myproj.lib.string_utils import reverse, is_palindrome, words, capitalize


def test_reverse_1(): assert reverse("python") == "nohtyp"
def test_reverse_2(): assert reverse("aa") == "aa"
def test_is_palindrome_1(): assert is_palindrome("dad") is True
def test_is_palindrome_2(): assert is_palindrome("hello") is False
def test_words_1(): assert words("x y z") == ["x", "y", "z"]
def test_capitalize_1(): assert capitalize("test") == "Test"
def test_reverse_3(): assert reverse("") == ""
def test_is_palindrome_3(): assert is_palindrome("noon") is True
def test_words_2(): assert words("single") == ["single"]
def test_capitalize_2(): assert capitalize("demo") == "Demo"
