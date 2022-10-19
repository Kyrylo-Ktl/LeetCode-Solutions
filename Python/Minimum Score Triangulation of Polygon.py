from functools import lru_cache
from typing import List


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n^2)
    """

    def minScoreTriangulation(self, values: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i + 1 >= j:
                return 0
            return min(
                dp(i, k) + dp(k, j) + values[i] * values[k] * values[j]
                for k in range(i + 1, j)
            )

        return dp(0, len(values) - 1)
