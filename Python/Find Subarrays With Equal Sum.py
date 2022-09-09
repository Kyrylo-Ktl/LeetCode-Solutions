from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()

        for i in range(len(nums) - 1):
            subarray = nums[i] + nums[i + 1]
            if subarray in sums:
                return True
            sums.add(subarray)

        return False
