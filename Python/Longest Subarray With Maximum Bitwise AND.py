from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        longest = current = 0

        for num in nums:
            if num == max_num:
                current += 1
            else:
                current = 0
            longest = max(longest, current)

        return longest
