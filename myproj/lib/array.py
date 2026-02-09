def sum_list(arr: list[int]) -> int:
    return sum(arr)


def unique(arr: list) -> list:
    return list(dict.fromkeys(arr))


def chunk(arr: list, size: int) -> list:
    return [arr[i : i + size] for i in range(0, len(arr), size)]


def flatten(arr: list) -> list:
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
