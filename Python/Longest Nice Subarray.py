from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = used_bits = j = 0

        for i, num in enumerate(nums):
            while used_bits & num != 0:
                used_bits ^= nums[j]
                j += 1

            used_bits |= num
            longest = max(longest, i - j + 1)

        return longest
