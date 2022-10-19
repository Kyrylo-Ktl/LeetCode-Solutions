from functools import lru_cache


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def minDistance(self, first: str, second: str) -> int:
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if not i or not j:
                return i or j

            if first[i - 1] == second[j - 1]:
                return dp(i - 1, j - 1)

            return min(
                dp(i, j - 1),
                dp(i - 1, j),
                dp(i - 1, j - 1)
            ) + 1

        m, n = len(first), len(second)
        return dp(m, n)


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n*m)
    """

    def minDistance(self, first: str, second: str) -> int:
        n, m = len(first), len(second)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if first[i - 1] == second[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                    ) + 1

        return dp[-1][-1]
