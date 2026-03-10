def capitalize(s: str) -> str:
    """Capitalize the first character of *s* and lowercase the rest.

    Unlike the built-in ``str.capitalize``, this function behaves identically
    to that method: the first character is uppercased and all subsequent
    characters are lowercased.  An empty string is returned unchanged.

    Args:
        s: The string to capitalize.

    Returns:
        A new string with the first character uppercased and the remainder
        lowercased.  Returns *s* unchanged if it is empty.
    """
    if not s:
        return s
    return s[0].upper() + s[1:].lower()


def reverse(s: str) -> str:
    """Return *s* with its characters in reverse order.

    Args:
        s: The string to reverse.

    Returns:
        A new string containing the same characters as *s* but in reverse
        order.
    """
    return s[::-1]


def truncate(s: str, max_len: int, suffix: str = "...") -> str:
    """Shorten *s* to at most *max_len* characters, appending *suffix* if cut.

    If *s* is already within the length limit it is returned unchanged.
    When truncation is necessary the returned string has exactly *max_len*
    characters: the leading ``max_len - len(suffix)`` characters of *s*
    followed by *suffix*.

    Args:
        s: The string to truncate.
        max_len: The maximum allowed length of the returned string (including
            the suffix when truncation occurs).
        suffix: The string appended to indicate truncation.  Defaults to
            ``"..."``.

    Returns:
        *s* unchanged if ``len(s) <= max_len``, otherwise a truncated string
        of length *max_len*.
    """
    if len(s) <= max_len:
        return s
    return s[: max_len - len(suffix)] + suffix


def words(s: str) -> list[str]:
    """Split *s* into a list of whitespace-delimited words.

    Leading and trailing whitespace is stripped before splitting, so multiple
    consecutive whitespace characters between words are collapsed into a
    single split point.

    Args:
        s: The string to split.

    Returns:
        A list of words.  Returns an empty list if *s* contains only
        whitespace.
    """
    return s.strip().split()


def is_palindrome(s: str) -> bool:
    """Return ``True`` if *s* reads the same forwards and backwards.

    The check is case-insensitive and ignores all non-alphanumeric characters,
    so punctuation and spaces do not affect the result.

    Args:
        s: The string to test.

    Returns:
        ``True`` if the alphanumeric content of *s* is a palindrome,
        ``False`` otherwise.
    """
    normalized = "".join(c.lower() for c in s if c.isalnum())
    return normalized == normalized[::-1]
