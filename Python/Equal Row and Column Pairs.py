from collections import defaultdict
from typing import List, Generator


class Solution:
    """
    Time:   O(n^3)
    Memory: O(1)
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pairs = 0

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if grid[i][k] != grid[k][j]:
                        break
                else:
                    pairs += 1

        return pairs


class Solution:
    """
    Time:   O(n^2)
    Memory: O(n)
    """

    def equalPairs(self, grid: List[List[int]]) -> int:
        mp = defaultdict(int)

        for col in zip(*grid):
            mp[self.serialize(col)] += 1

        return sum(mp[self.serialize(row)] for row in grid)

    @staticmethod
    def serialize(nums: Generator) -> str:
        return ','.join(map(str, nums))
