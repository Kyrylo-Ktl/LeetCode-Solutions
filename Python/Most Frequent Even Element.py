from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = (n for n in nums if not n & 1)
        count = Counter(even_nums)
        return max(count, key=lambda x: (count[x], -x)) if count else -1
