from myproj.utils.validation import is_email, is_non_empty, in_range


def test_is_email_complex():
    assert is_email("user.name+tag@example.co.uk") is True


def test_in_range_inclusive():
    assert in_range(0, 0, 10) is True
    assert in_range(10, 0, 10) is True
