from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    """
    Time:   O(n*√n)
    Memory: O(n)
    """

    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = defaultdict(int)

        longest = 1
        for i in sorted(nums):
            root = sqrt(i)

            if root.is_integer():
                dp[i] = dp[int(root)] + 1
                longest = max(longest, dp[i])
            else:
                dp[i] = 1

        return -1 if longest < 2 else longest
