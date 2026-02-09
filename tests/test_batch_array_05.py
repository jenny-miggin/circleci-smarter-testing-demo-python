from myproj.lib.array import sum_list, unique, chunk, flatten


def test_sum_list_1(): assert sum_list([11, 22]) == 33
def test_unique_1(): assert unique([7, 8, 7, 9]) == [7, 8, 9]
def test_chunk_1(): assert chunk([1, 2, 3, 4, 5], 1) == [[1], [2], [3], [4], [5]]
def test_flatten_1(): assert flatten([[1], [2], [3], [4]]) == [1, 2, 3, 4]
def test_sum_list_2(): assert sum_list([1, 2, 3, 4, 5]) == 15
def test_unique_2(): assert unique(["x", "y", "x"]) == ["x", "y"]
def test_chunk_2(): assert chunk([1, 2, 3], 3) == [[1, 2, 3]]
def test_flatten_2(): assert flatten([[1, 2]]) == [1, 2]
def test_sum_list_3(): assert sum_list([9, 9]) == 18
def test_chunk_3(): assert chunk([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
