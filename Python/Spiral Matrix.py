from typing import List


class Solution:
    """
    Time:   O(?)
    Memory: O(?)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        return matrix.pop(0) + self.spiralOrder(list(map(list, zip(*matrix)))[::-1])
