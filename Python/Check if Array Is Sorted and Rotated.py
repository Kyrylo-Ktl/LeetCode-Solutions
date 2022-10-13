from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                return nums[0] >= nums[-1] and all(nums[j] <= nums[j + 1] for j in range(i, n - 1))

        return True
