from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums) - 1):
            if increasing and nums[i] > nums[i + 1]:
                increasing = False
            if decreasing and nums[i] < nums[i + 1]:
                decreasing = False

        return increasing or decreasing
