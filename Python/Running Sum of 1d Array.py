from itertools import accumulate
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def runningSum(self, nums: List[int]):
        return accumulate(nums)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
