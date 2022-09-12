from typing import Generator, List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n+m)
    """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        return all(len(set(diag)) == 1 for diag in self._diagonals_generator(matrix))

    @staticmethod
    def _diagonals_generator(matrix: List[List[int]]) -> Generator:
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            yield [matrix[i + k][k] for k in range(min(m, n - i))]
        for j in range(1, m):
            yield [matrix[k][j + k] for k in range(min(m - j, n))]


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n, m = len(matrix), len(matrix[0])
        return all(matrix[i][j] == matrix[i + 1][j + 1] for i in range(n - 1) for j in range(m - 1))
