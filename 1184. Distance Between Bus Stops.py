from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        i, j = sorted((start, destination))
        clockwise = sum(distance[i:j])
        counterclockwise = sum(distance[:i] + distance[j:])
        return min(clockwise, counterclockwise)
