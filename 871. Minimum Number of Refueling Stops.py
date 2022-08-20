from heapq import heappop, heappush
from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def minRefuelStops(self, target: int, tank: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append([target, maxsize])

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev

            while pq and tank < 0:
                tank += -heappop(pq)
                ans += 1
            if tank < 0:
                return -1

            heappush(pq, -capacity)
            prev = location

        return ans
