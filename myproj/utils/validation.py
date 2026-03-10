import re


def is_email(s: str) -> bool:
    """Return ``True`` if *s* looks like a valid e-mail address.

    The check uses a simple regular expression that requires:

    - One or more non-whitespace, non-``@`` characters before the ``@``.
    - One or more non-whitespace, non-``@`` characters for the domain label.
    - A literal ``.``.
    - One or more non-whitespace, non-``@`` characters for the TLD.

    This is intentionally lenient and does **not** fully validate RFC 5322
    compliance.

    Args:
        s: The string to test.

    Returns:
        ``True`` if *s* matches the e-mail pattern, ``False`` otherwise.
    """
    return bool(re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", s))


def is_non_empty(s: str) -> bool:
    """Return ``True`` if *s* is a string containing at least one non-space character.

    Args:
        s: The value to check.  Values that are not strings always return
            ``False``.

    Returns:
        ``True`` if *s* is a ``str`` and ``s.strip()`` is non-empty,
        ``False`` otherwise.
    """
    return isinstance(s, str) and s.strip() != ""


def in_range(n: float, min_val: float, max_val: float) -> bool:
    """Return ``True`` if *n* lies within the closed interval [*min_val*, *max_val*].

    Args:
        n: The number to test.
        min_val: The inclusive lower bound of the interval.
        max_val: The inclusive upper bound of the interval.

    Returns:
        ``True`` if ``min_val <= n <= max_val``, ``False`` otherwise.
    """
    return min_val <= n <= max_val
