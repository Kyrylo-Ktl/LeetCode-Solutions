from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def fillCups(self, amount: List[int]) -> int:
        c, w, h = amount
        return max(max(c, w, h), (c + w + h + 1) // 2)
