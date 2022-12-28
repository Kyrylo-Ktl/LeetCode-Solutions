from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    """
    Time:   O(n*log2(n))
    Memory: O(n)
    """

    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []

        for p in piles:
            heappush(heap, -p)

        for _ in range(k):
            p = heappop(heap)
            heappush(heap, p // 2)

        return -sum(heap)


class Solution:
    """
    Time:   O(n*log2(n))
    Memory: O(1)
    """

    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i, p in enumerate(piles):
            piles[i] = -p

        heapify(piles)

        for _ in range(k):
            p = heappop(piles)
            heappush(piles, p // 2)

        return -sum(piles)
