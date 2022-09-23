from functools import lru_cache
from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0

            sign, operation = (1, max) if (j - i - n) & 1 else (-1, min)

            return operation(
                sign * piles[i] + dp(i + 1, j),
                sign * piles[j] + dp(i, j - 1),
            )

        n = len(piles)
        return dp(0, n - 1) > 0


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def stoneGame(self, piles: List[int]) -> bool:
        return True

