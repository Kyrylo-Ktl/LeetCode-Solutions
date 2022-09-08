from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0

        for i in range(len(nums)):
            if i == 0 or nums[i - 1] != nums[i]:
                nums[pos] = nums[i]
                pos += 1

        return pos
