from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    MAX_DUPLICATES = 2

    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for num in nums:
            if i < self.MAX_DUPLICATES or nums[i - self.MAX_DUPLICATES] != num:
                nums[i] = num
                i += 1

        return i
