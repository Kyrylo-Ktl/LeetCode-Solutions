from heapq import heappush, heappop
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    MOD = 10 ** 9 + 7

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        res = total_sum = 0
        heap = []

        for e, s in sorted(zip(efficiency, speed), reverse=True):
            heappush(heap, s)
            total_sum += s
            if len(heap) > k:
                total_sum -= heappop(heap)
            res = max(res, total_sum * e)

        return res % self.MOD
