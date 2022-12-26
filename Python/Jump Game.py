from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0

        for i, num in enumerate(nums):
            if i > max_ind:
                return False
            max_ind = max(max_ind, i + num)

        return True
