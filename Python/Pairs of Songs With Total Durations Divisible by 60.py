from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo = defaultdict(int)
        count = 0

        for t in time:
            count += memo[-t % 60]
            memo[t % 60] += 1

        return count
