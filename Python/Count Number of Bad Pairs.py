from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def countBadPairs(self, nums: List[int]) -> int:
        return sum(x * (len(nums) - x) for x in Counter(i - num for i, num in enumerate(nums)).values()) // 2
