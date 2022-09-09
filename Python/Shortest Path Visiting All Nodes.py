from collections import deque
from typing import List


class Solution:
    """
    Time:   O(n^2*2^n)
    Memory: O(n*2^n)
    """

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        target_state = (1 << n) - 1
        queue = deque([(node, 1 << node) for node in range(n)])
        seen = set(queue)

        steps = 0
        while queue:
            for _ in range(len(queue)):
                u, state = queue.popleft()

                if state == target_state:
                    return steps

                for v in graph[u]:
                    next_state = state | (1 << v)
                    if (v, next_state) not in seen:
                        seen.add((v, next_state))
                        queue.append((v, next_state))
            steps += 1
