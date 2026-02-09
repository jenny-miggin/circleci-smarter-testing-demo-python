from myproj.lib.math import add, subtract, multiply, divide


def evaluate(expr: str) -> float:
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
