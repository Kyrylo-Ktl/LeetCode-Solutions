from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = 1

        for n in nums:
            if nums[abs(n) - 1] < 0:
                duplicate = abs(n)
            else:
                nums[abs(n) - 1] *= -1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                missing = i + 1

        return [duplicate, missing]
