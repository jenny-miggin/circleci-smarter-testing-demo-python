def sum_list(arr: list[int]) -> int:
    """Return the sum of all integers in *arr*.

    Args:
        arr: A list of integers to sum.

    Returns:
        The total sum of all elements.  Returns ``0`` for an empty list.
    """
    return sum(arr)


def unique(arr: list) -> list:
    """Return a deduplicated copy of *arr* preserving insertion order.

    Duplicate values are removed while keeping the first occurrence of each
    element.

    Args:
        arr: The source list (elements must be hashable).

    Returns:
        A new list containing only the first occurrence of each value.
    """
    return list(dict.fromkeys(arr))


def chunk(arr: list, size: int) -> list:
    """Split *arr* into consecutive sub-lists of length *size*.

    The last chunk may be shorter than *size* if the list length is not
    evenly divisible by *size*.

    Args:
        arr: The list to split.
        size: The maximum number of elements per chunk.  Must be a positive
            integer.

    Returns:
        A list of sub-lists, each containing at most *size* elements.
    """
    return [arr[i : i + size] for i in range(0, len(arr), size)]


def flatten(arr: list) -> list:
    """Recursively flatten a nested list into a single flat list.

    Only ``list`` instances are unwrapped; other iterables (e.g. tuples,
    strings) are treated as atomic values and appended as-is.

    Args:
        arr: A potentially nested list.

    Returns:
        A new flat list containing all non-list leaf elements in depth-first
        order.
    """
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
