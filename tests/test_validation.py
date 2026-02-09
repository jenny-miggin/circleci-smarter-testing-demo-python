from myproj.utils.validation import is_email, is_non_empty, in_range


def test_is_email():
    assert is_email("a@b.co") is True
    assert is_email("invalid") is False


def test_is_non_empty():
    assert is_non_empty("  x  ") is True
    assert is_non_empty("   ") is False


def test_in_range():
    assert in_range(5, 0, 10) is True
    assert in_range(11, 0, 10) is False
