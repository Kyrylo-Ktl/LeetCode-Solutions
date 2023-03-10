from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sub_arrays = l = 0

        for r, num in enumerate(nums):
            if num != 0:
                l = r + 1
            sub_arrays += r - l + 1

        return sub_arrays
