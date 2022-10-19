from functools import lru_cache


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(log(n))
    """

    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=self.power)[k - 1]

    @classmethod
    @lru_cache(maxsize=None)
    def power(cls, n: int) -> int:
        if n == 1:
            return 1
        return cls.power(3 * n + 1 if n & 1 else n >> 1) + 1
