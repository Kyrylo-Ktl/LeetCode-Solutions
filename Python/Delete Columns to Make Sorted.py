from typing import List


class Solution:
    """
    Time:   O(m*n*log2(n))
    Memory: O(n)
    """

    def minDeletionSize(self, grid: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*grid))
