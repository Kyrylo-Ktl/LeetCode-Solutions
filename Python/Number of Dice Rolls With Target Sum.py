from functools import lru_cache


class Solution:
    """
    Time:   O(n*k)
    Memory: O(n*k)
    """

    MOD = 10 ** 9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @lru_cache(None)
        def dp(d: int, t: int) -> int:
            if d == 0:
                return int(t == 0)
            return sum(dp(d - 1, t - i) for i in range(1, k + 1)) % self.MOD

        return dp(n, target)
