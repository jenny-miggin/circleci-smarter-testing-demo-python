from myproj.lib.array import sum_list, unique, chunk, flatten


def test_sum_list_empty():
    assert sum_list([]) == 0


def test_chunk_single():
    assert chunk([1, 2, 3], 10) == [[1, 2, 3]]


def test_flatten_nested():
    assert flatten([[1], [2, [3, 4]]]) == [1, 2, 3, 4]
