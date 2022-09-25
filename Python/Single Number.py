from functools import reduce
from operator import xor
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
