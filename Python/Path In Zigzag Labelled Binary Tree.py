from typing import List


class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def pathInZigZagTree(self, label: int) -> List[int]:
        level = 0
        while 1 << level <= label:
            level += 1

        path = [-1] * level
        for i in range(level, 0, -1):
            path[i - 1] = label
            label = ((1 << i) - 1 - label + (1 << (i - 1))) // 2

        return path
