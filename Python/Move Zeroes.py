from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for cur, num in enumerate(nums):
            if num != 0:
                nums[cur], nums[last_non_zero] = nums[last_non_zero], num
                last_non_zero += 1
