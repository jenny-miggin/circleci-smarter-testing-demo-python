from myproj.lib.array import sum_list, unique, chunk, flatten


def test_sum_list_1(): assert sum_list([4, 5, 6]) == 15
def test_unique_1(): assert unique([1, 2, 3, 1]) == [1, 2, 3]
def test_unique_2(): assert unique(["a", "b", "a"]) == ["a", "b"]
def test_chunk_1(): assert chunk([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
def test_chunk_2(): assert chunk([1, 2, 3], 5) == [[1, 2, 3]]
def test_flatten_1(): assert flatten([[1, 2], [3]]) == [1, 2, 3]
def test_flatten_2(): assert flatten([[]]) == []
def test_sum_list_2(): assert sum_list([1, 1, 1]) == 3
def test_chunk_3(): assert chunk([1], 2) == [[1]]
def test_unique_3(): assert unique([]) == []
