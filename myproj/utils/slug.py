import re


def slugify(s: str) -> str:
    """Convert a string into a URL-friendly slug.

    The conversion applies the following transformations in order:

    1. Strip leading/trailing whitespace and convert to lowercase.
    2. Replace one or more whitespace characters with a single hyphen.
    3. Remove any character that is not a lowercase letter, digit, or hyphen.
    4. Collapse consecutive hyphens into one and strip leading/trailing hyphens.

    Args:
        s: The input string to slugify (e.g. a page title).

    Returns:
        A lowercase, hyphen-separated slug containing only ``[a-z0-9-]``
        characters with no leading, trailing, or consecutive hyphens.

    Examples:
        >>> slugify("Hello World!")
        'hello-world'
        >>> slugify("  Multiple   Spaces  ")
        'multiple-spaces'
    """
    s = s.lower().strip()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s


def deslugify(s: str) -> str:
    """Convert a slug back into a human-readable string.

    Replaces every hyphen in *s* with a space.  No other transformations are
    applied (e.g. capitalisation is not restored).

    Args:
        s: A slug string (e.g. ``"hello-world"``).

    Returns:
        The slug with hyphens replaced by spaces (e.g. ``"hello world"``).

    Examples:
        >>> deslugify("hello-world")
        'hello world'
    """
    return s.replace("-", " ")
