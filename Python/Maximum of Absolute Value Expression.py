from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def maxAbsValExpr(self, a: List[int], b: List[int]) -> int:
        points = [
            (
                x + y + i,
                x + y - i,
                x - y + i,
                x - y - i
            )
            for i, (x, y) in enumerate(zip(a, b))
        ]
        return max(max(dim) - min(dim) for dim in zip(*points))
