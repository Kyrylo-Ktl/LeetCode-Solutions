from functools import lru_cache
from typing import List


class Solution:
    """
    Time:   O(n*t)
    Memory: O(n*t)

    where t - sum of nums list
    """

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dp(i: int, curr_sum: int) -> int:
            if i < 0:
                return int(curr_sum == target)
            return dp(i - 1, curr_sum - nums[i]) + \
                   dp(i - 1, curr_sum + nums[i])

        return dp(len(nums) - 1, 0)
