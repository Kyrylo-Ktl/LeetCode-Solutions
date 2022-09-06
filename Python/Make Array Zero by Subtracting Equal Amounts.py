from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num != 0})
