from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [nums[j] for i in range(n) for j in (i, i + n)]
