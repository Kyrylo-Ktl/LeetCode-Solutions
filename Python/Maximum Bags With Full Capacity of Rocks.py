from typing import List


class Solution:
    """
    Time:   O(n*log2(n))
    Memory: O(n)
    """

    def maximumBags(self, capacity: List[int], rocks: List[int], additional_rocks: int) -> int:
        count = sorted((c - r for c, r in zip(capacity, rocks)), reverse=True)

        while count and additional_rocks and count[-1] <= additional_rocks:
            additional_rocks -= count.pop()

        return len(rocks) - len(count)
