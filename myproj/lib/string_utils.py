def capitalize(s: str) -> str:
    if not s:
        return s
    return s[0].upper() + s[1:].lower()


def reverse(s: str) -> str:
    return s[::-1]


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def words(s: str) -> list[str]:
    return s.strip().split()


def is_palindrome(s: str) -> bool:
    normalized = "".join(c.lower() for c in s if c.isalnum())
    return normalized == normalized[::-1]
