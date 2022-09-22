from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = maxsize
        window_sum = start = 0

        for end, num in enumerate(nums):
            window_sum += num
            while window_sum >= target:
                min_len = min(min_len, end - start + 1)
                window_sum -= nums[start]
                start += 1

        return min_len if min_len != maxsize else 0
