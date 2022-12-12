from functools import lru_cache


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def ways(i: int) -> int:
            if i > n:
                return 0
            elif i == n:
                return 1
            return ways(i + 1) + ways(i + 2)

        return ways(0)
