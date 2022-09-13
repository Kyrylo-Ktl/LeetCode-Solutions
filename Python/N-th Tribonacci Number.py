from functools import lru_cache


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    @lru_cache(maxsize=None)
    def tribonacci(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 3:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return a

