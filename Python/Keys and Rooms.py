from collections import deque
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        unvisited = set(range(len(rooms)))

        while queue:
            v = queue.popleft()
            if v in unvisited:
                unvisited.remove(v)
                queue.extend(rooms[v])

        return not unvisited
