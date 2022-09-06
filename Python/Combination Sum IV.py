from functools import lru_cache
from typing import List


class Solution:
    """
    Time:   O(2^n)
    Memory: O(n)
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dp(target: int) -> int:
            if target == 0:
                return 1
            if target < 0:
                return 0
            return sum(dp(target - num) for num in nums)

        return dp(target)
