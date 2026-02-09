def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def multiply_yet_another(a: int, b: int) -> int:
    return a * b * 100


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def clamp(value: int, min_val: int, max_val: int) -> int:
    return max(min_val, min(max_val, value))
