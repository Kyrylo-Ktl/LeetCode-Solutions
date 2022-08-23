from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        x = tops[0]
        if all(x == a or x == b for a, b in zip(tops, bottoms)):
            return len(tops) - max(tops.count(x), bottoms.count(x))

        x = bottoms[0]
        if all(x == a or x == b for a, b in zip(tops, bottoms)):
            return len(tops) - max(tops.count(x), bottoms.count(x))

        return -1
