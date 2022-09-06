class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def computeArea(self, *coords) -> int:
        x1, y1, x2, y2, x3, y3, x4, y4 = coords
        overlap = max(min(x2, x4) - max(x1, x3), 0) * max(min(y2, y4) - max(y1, y3), 0)
        return (x2 - x1) * (y2 - y1) + (x4 - x3) * (y4 - y3) - overlap
