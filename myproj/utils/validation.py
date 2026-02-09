import re


def is_email(s: str) -> bool:
    return bool(re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", s))


def is_non_empty(s: str) -> bool:
    return isinstance(s, str) and s.strip() != ""


def in_range(n: float, min_val: float, max_val: float) -> bool:
    return min_val <= n <= max_val
