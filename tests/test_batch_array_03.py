from myproj.lib.array import sum_list, unique, chunk, flatten


def test_sum_list_1(): assert sum_list([7, 8, 9]) == 24
def test_sum_list_2(): assert sum_list([100]) == 100
def test_unique_1(): assert unique([3, 2, 1, 2]) == [3, 2, 1]
def test_chunk_1(): assert chunk([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
def test_chunk_2(): assert chunk([a for a in range(4)], 1) == [[0], [1], [2], [3]]
def test_flatten_1(): assert flatten([[1], [2], [3]]) == [1, 2, 3]
def test_flatten_2(): assert flatten([[1, [2, 3]]]) == [1, 2, 3]
def test_sum_list_3(): assert sum_list([0, 0, 0]) == 0
def test_unique_2(): assert unique([1]) == [1]
def test_chunk_3(): assert chunk([1, 2], 1) == [[1], [2]]
