from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(1)
    """

    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = -maxsize
        partitions = 0

        for num in nums:
            if num - start > k:
                start = num
                partitions += 1

        return partitions
