from bisect import bisect_left
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for x in nums:
            if not seq or seq[-1] < x:
                seq.append(x)
            else:
                seq[bisect_left(seq, x)] = x

        return len(seq)
