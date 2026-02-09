from myproj.lib.array import sum_list, unique, chunk, flatten


def test_sum_list():
    assert sum_list([1, 2, 3]) == 6


def test_unique():
    assert unique([1, 2, 2, 3, 1]) == [1, 2, 3]


def test_chunk():
    assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]


def test_flatten():
    assert flatten([[1, 2], [3]]) == [1, 2, 3]
