from typing import List


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def isRectangleOverlap(self, rectangle_a: List[int], rectangle_b: List[int]) -> bool:
        x1, y1, x2, y2 = rectangle_a
        x3, y3, x4, y4 = rectangle_b
        return x1 < x4 and x3 < x2 and y1 < y4 and y3 < y2
