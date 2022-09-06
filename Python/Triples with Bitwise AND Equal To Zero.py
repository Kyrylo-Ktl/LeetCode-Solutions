from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n^3)
    Memory: O(n^2)
    """

    def countTriplets(self, nums: List[int]) -> int:
        count = Counter(x & y for x in nums for y in nums)
        return sum(cnt for xy, cnt in count.items() for z in nums if not xy & z)
