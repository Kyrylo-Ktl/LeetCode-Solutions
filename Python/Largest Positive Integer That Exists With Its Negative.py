from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def findMaxK(self, nums: List[int]) -> int:
        uniq = set(nums)
        return max((num for num in uniq if -num in uniq), default=-1)


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] == -nums[j]:
                return nums[j]
            if abs(nums[i]) > abs(nums[j]):
                i += 1
            else:
                j -= 1

        return -1
