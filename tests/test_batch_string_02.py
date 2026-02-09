from myproj.lib.string_utils import capitalize, reverse, truncate, words


def test_capitalize_1(): assert capitalize("world") == "World"
def test_capitalize_2(): assert capitalize("") == ""
def test_reverse_1(): assert reverse("test") == "tset"
def test_reverse_2(): assert reverse("a") == "a"
def test_truncate_1(): assert truncate("long string here", 8) == "long s..."
def test_truncate_2(): assert truncate("exact", 5) == "exact"
def test_words_1(): assert words("one two three") == ["one", "two", "three"]
def test_words_2(): assert words("  spaced  ") == ["spaced"]
def test_capitalize_3(): assert capitalize("PYTHON") == "Python"
def test_reverse_3(): assert reverse("123") == "321"
