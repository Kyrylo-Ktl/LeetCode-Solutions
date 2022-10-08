from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0

        for i, x in enumerate(colors):
            if x != colors[0]:
                max_dist = max(max_dist, i)
            if x != colors[-1]:
                max_dist = max(max_dist, len(colors) - 1 - i)

        return max_dist
