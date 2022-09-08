from functools import lru_cache
from math import isqrt


class Solution:
    """
    Time:   O(n*√n)
    Memory: O(n)
    """

    def numSquares(self, n: int) -> int:
        return self._decompose(n)

    @classmethod
    @lru_cache(None)
    def _decompose(cls, n: int) -> int:
        if n < 2:
            return n
        return 1 + min(cls._decompose(n - i * i) for i in range(1, isqrt(n) + 1))
