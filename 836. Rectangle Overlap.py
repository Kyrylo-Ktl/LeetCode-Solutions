from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def isRectangleOverlap(self, rectangle_a: List[int], rectangle_b: List[int]) -> bool:
        x1, y1, x2, y2 = rectangle_a
        x3, y3, x4, y4 = rectangle_b
        return min(x2, x4) - max(x1, x3) > 0 and \
               min(y2, y4) - max(y1, y3) > 0
