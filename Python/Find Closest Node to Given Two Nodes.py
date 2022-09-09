from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def closestMeetingNode(self, edges: List[int], a: int, b: int) -> int:
        def dfs(u: int, arr: list, dist: int = 0):
            while arr[u] == -1 and u != -1:
                arr[u] = dist
                dfs(edges[u], arr, dist + 1)

        n = len(edges)

        a_distances = [-1] * n
        dfs(a, a_distances)

        b_distances = [-1] * n
        dfs(b, b_distances)

        min_node = -1
        min_dist = maxsize

        for i, (a_dict, b_dist) in enumerate(zip(a_distances, b_distances)):
            if a_dict == -1 or b_dist == -1:
                continue

            distance = max(a_dict, b_dist)

            if distance < min_dist:
                min_dist = distance
                min_node = i

        return min_node
