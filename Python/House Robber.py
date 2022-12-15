from functools import cache
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def rob(self, nums: List[int]) -> int:
        @cache
        def dp(i: int) -> int:
            if i < 0:
                return 0
            return max(dp(i - 1), dp(i - 2) + nums[i])

        return dp(len(nums) - 1)
