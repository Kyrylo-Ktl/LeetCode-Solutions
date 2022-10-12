from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            if nums[i + 2] + nums[i + 1] > nums[i]:
                return nums[i + 2] + nums[i + 1] + nums[i]

        return 0
