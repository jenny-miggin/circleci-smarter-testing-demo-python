from myproj.lib.math import add, subtract, multiply, divide


def evaluate(expr: str) -> float:
    """Evaluate a simple infix arithmetic expression and return the result.

    The expression must consist of exactly three whitespace-separated tokens:

    ``<number> <operator> <number>``

    Supported operators are ``+``, ``-``, ``*``, and ``/``.  Both operands
    are first parsed as floats and then truncated to ``int`` before being
    passed to the underlying math functions.

    Args:
        expr: A string expression such as ``"3 + 4"`` or ``"10 / 2"``.

    Returns:
        The numeric result of the expression as a ``float``.

    Raises:
        ValueError: If *expr* does not contain exactly three tokens, if an
            unknown operator is provided, or if division by zero is attempted.

    Examples:
        >>> evaluate("3 + 4")
        7
        >>> evaluate("10 / 4")
        2.5
    """
    parts = expr.strip().split()
    if len(parts) != 3:
        raise ValueError("Expected 'a op b'")
    a, op, b = float(parts[0]), parts[1], float(parts[2])
    if op == "+":
        return add(int(a), int(b))
    if op == "-":
        return subtract(int(a), int(b))
    if op == "*":
        return multiply(int(a), int(b))
    if op == "/":
        return divide(int(a), int(b))
    raise ValueError(f"Unknown operator: {op}")
