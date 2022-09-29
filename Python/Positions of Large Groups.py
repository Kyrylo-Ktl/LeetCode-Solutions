from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    MIN_GROUP_LENGTH = 3

    def largeGroupPositions(self, s: str) -> List[List[int]]:
        positions = []
        n = len(s)
        j = 0

        for i in range(n):
            if i == n - 1 or s[i] != s[i + 1]:
                if i - j + 1 >= self.MIN_GROUP_LENGTH:
                    positions.append([j, i])
                j = i + 1

        return positions
