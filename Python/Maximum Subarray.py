from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, curr_sum = -maxsize, 0

        for num in nums:
            curr_sum += num
            if max_sum < curr_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0

        return max_sum
