from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def arrayNesting(self, nums: List[int]) -> int:
        seen = [False] * len(nums)
        max_length = 0

        for k in nums:
            length = 0
            while not seen[k]:
                seen[k], length, k = True, length + 1, nums[k]
            max_length = max(max_length, length)

        return max_length
