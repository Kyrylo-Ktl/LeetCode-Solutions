from typing import List


class Solution:
    """
    Time:   O(n*log2(n))
    Memory: O(1)
    """

    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum((coins := coins - cost) >= 0 for cost in sorted(costs))
