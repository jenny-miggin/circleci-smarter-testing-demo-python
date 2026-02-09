from myproj.api.handlers import handle_sum, handle_validate_email


def test_handle_sum():
    assert handle_sum({"a": 1, "b": 2}) == {"result": 3}
    assert handle_sum({}) == {"result": 0}


def test_handle_validate_email():
    assert handle_validate_email({"email": "a@b.co"}) == {"valid": True}
    assert handle_validate_email({"email": "x"}) == {"valid": False}
