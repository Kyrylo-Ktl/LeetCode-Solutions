from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(1)
    """

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        for i in range(1, n):
            for j in range(m):
                matrix[i][j] += min(
                    matrix[i - 1][max(    0, j - 1)],
                    matrix[i - 1][j],
                    matrix[i - 1][min(m - 1, j + 1)],
                )

        return min(matrix[-1])
