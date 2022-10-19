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
