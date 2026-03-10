def add(a: int, b: int) -> int:
    """Return the sum of two integers.

    Args:
        a: The first operand.
        b: The second operand.

    Returns:
        The arithmetic sum of *a* and *b*.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two integers.

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        The result of subtracting *b* from *a*.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two integers.

    Args:
        a: The first factor.
        b: The second factor.

    Returns:
        The arithmetic product of *a* and *b*.
    """
    return a * b


def multiply_yet_another(a: int, b: int) -> int:
    """Return the product of two integers scaled by 100.

    This is a convenience function that multiplies *a* by *b* and then
    multiplies the result by 100.

    Args:
        a: The first factor.
        b: The second factor.

    Returns:
        ``a * b * 100``
    """
    return a * b * 100


def divide(a: int, b: int) -> float:
    """Return the quotient of two integers.

    Args:
        a: The dividend.
        b: The divisor.  Must not be zero.

    Returns:
        The floating-point result of dividing *a* by *b*.

    Raises:
        ValueError: If *b* is zero.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def clamp(value: int, min_val: int, max_val: int) -> int:
    """Clamp *value* to the closed interval [*min_val*, *max_val*].

    Args:
        value: The integer to clamp.
        min_val: The lower bound of the interval (inclusive).
        max_val: The upper bound of the interval (inclusive).

    Returns:
        *value* unchanged if it already lies within the interval; otherwise
        *min_val* if *value* is below the interval, or *max_val* if *value*
        is above the interval.
    """
    return max(min_val, min(max_val, value))
