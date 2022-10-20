from functools import lru_cache
from math import comb


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def uniquePaths(self, n: int, m: int) -> int:
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 1
            return dp(i - 1, j) + dp(i, j - 1)

        return dp(n - 1, m - 1)


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def uniquePaths(self, n: int, m: int) -> int:
        dp = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


class Solution:
    """
    Time:   O(n+m)
    Memory: O(1)
    """

    def uniquePaths(self, n: int, m: int) -> int:
        return comb(n + m - 2, m - 1)
