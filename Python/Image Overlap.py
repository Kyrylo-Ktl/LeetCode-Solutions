from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n^4)
    Memory: O(1)
    """

    def largestOverlap(self, a: List[List[int]], b: List[List[int]]) -> int:
        a_ones_coords = [(x, y) for x, row in enumerate(a) for y, item in enumerate(row) if item]
        b_ones_coords = [(x, y) for x, row in enumerate(b) for y, item in enumerate(row) if item]
        shifts = Counter((ax - bx, ay - by) for ax, ay in a_ones_coords for bx, by in b_ones_coords)
        return max(shifts.values(), default=0)
