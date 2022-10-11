from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        return [[matrix[i][j] for i in range(n)] for j in range(m)]


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
