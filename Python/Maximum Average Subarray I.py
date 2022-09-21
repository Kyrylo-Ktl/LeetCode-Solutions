from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = cur_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k
