from functools import cache


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def longestCommonSubsequence(self, first: str, second: str) -> int:
        @cache
        def lcs(i: int, j: int) -> int:
            if i == 0 or j == 0:
                return 0
            if first[i - 1] == second[j - 1]:
                return 1 + lcs(i - 1, j - 1)
            return max(lcs(i - 1, j), lcs(i, j - 1))

        return lcs(len(first), len(second))


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def longestCommonSubsequence(self, first: str, second: str) -> int:
        n, m = len(first), len(second)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
