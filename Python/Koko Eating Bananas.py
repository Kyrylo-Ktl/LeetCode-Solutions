from math import ceil
from typing import List


class Solution:
    """
    Time:   O(n*log(M))
    Memory: O(1)
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def f(k: int) -> int:
            return sum(ceil(p / k) for p in piles)

        lo, hi = 1, 1_000_000_000

        while lo < hi:
            mid = (lo + hi) // 2

            if f(mid) > h:
                lo = mid + 1
            else:
                hi = mid

        return lo
