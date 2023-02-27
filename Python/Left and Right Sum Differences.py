from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_sum = [0] * n
        for i in range(n - 1, 0, -1):
            left_sum[i - 1] = left_sum[i] + nums[i]

        right_sum = [0] * n
        for i in range(n - 1):
            right_sum[i + 1] = right_sum[i] + nums[i]

        return [abs(l - r) for l, r in zip(left_sum, right_sum)]
