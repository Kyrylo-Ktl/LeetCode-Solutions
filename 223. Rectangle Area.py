class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def computeArea(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> int:
        overlap = max(min(x2, x4) - max(x1, x3), 0) * max(min(y2, y4) - max(y1, y3), 0)
        return (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3) - overlap
