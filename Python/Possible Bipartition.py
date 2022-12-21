from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(V+E)
    Memory: O(V+E)
    """

    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def dfs(i: int, curr_color: bool) -> bool:
            color[i] = curr_color

            for j in graph[i]:
                if color[j] is curr_color:
                    return False

                if color[j] is None and (not dfs(j, not curr_color)):
                    return False

            return True

        if n == 1 or not dislikes:
            return True

        graph = defaultdict(list)
        color = defaultdict(lambda: None)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for person_id in range(1, n + 1):
            if color[person_id] is None and not dfs(person_id, True):
                return False

        return True
