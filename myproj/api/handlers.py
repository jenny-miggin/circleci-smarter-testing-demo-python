from myproj.lib.math import add
from myproj.utils.validation import is_email


def handle_sum(body: dict) -> dict:
    """Handle a request to add two numbers.

    Reads ``"a"`` and ``"b"`` from *body*, converts them to ``int``, and
    returns their sum.  Missing keys default to ``0``.

    Args:
        body: A mapping that may contain the keys ``"a"`` and ``"b"``.
            Values are cast to ``int`` before addition.

    Returns:
        A dict of the form ``{"result": <int>}`` containing the sum of *a*
        and *b*.
    """
    a = body.get("a", 0)
    b = body.get("b", 0)
    return {"result": add(int(a), int(b))}


def handle_validate_email(body: dict) -> dict:
    """Handle a request to validate an e-mail address.

    Reads ``"email"`` from *body* and returns whether it passes basic e-mail
    format validation.  A missing key is treated as an empty string, which
    always fails validation.

    Args:
        body: A mapping that may contain the key ``"email"``.  The value is
            cast to ``str`` before validation.

    Returns:
        A dict of the form ``{"valid": <bool>}`` where ``True`` means the
        address looks valid.
    """
    email = body.get("email", "")
    return {"valid": is_email(str(email))}
