from functools import lru_cache
from typing import List


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def max_path(i: int, j: int) -> int:
            val = matrix[i][j]
            return 1 + max(
                max_path(i + 1, j) if i + 1 < n and val < matrix[i + 1][j] else 0,
                max_path(i - 1, j) if     i > 0 and val < matrix[i - 1][j] else 0,
                max_path(i, j + 1) if j + 1 < m and val < matrix[i][j + 1] else 0,
                max_path(i, j - 1) if     j > 0 and val < matrix[i][j - 1] else 0,
            )

        n, m = len(matrix), len(matrix[0])
        return max(max_path(row, col) for row in range(n) for col in range(m))
