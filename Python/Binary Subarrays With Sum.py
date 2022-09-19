from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def numSubarraysWithSum(self, nums: List[int], target: int) -> int:
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        sub_arrays = 0
        for prefix in accumulate(nums):
            sub_arrays += prefix_sums[prefix - target]
            prefix_sums[prefix] += 1

        return sub_arrays
