from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def minimumDifference(self, nums: List[int], k: int) -> int:
        min_diff = maxsize
        nums.sort()

        for i in range(k - 1, len(nums)):
            min_diff = min(min_diff, nums[i] - nums[i - k + 1])

        return min_diff
