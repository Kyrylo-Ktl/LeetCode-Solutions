from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        seen = [False] * n

        for _, to in edges:
            seen[to] = True

        return [v for v, is_seen in enumerate(seen) if not is_seen]
