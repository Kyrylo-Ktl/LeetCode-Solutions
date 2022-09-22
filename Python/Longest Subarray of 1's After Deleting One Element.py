from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestSubarray(self, nums: List[int]) -> int:
        longest = prev = curr = 0

        for bit in nums:
            if bit:
                curr += 1
                longest = max(longest, prev + curr)
            else:
                prev, curr = curr, 0

        return longest - (longest == len(nums))
