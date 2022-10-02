from collections import deque
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    NEIGHBOURS = {
        str(i): (str((i + 1) % 10), str((i - 1) % 10))
        for i in range(10)
    }

    def openLock(self, deadends: List[str], target: str) -> int:
        n = len(target)
        start = '0' * n

        if start in deadends:
            return -1

        queue = deque([(start, 0)])
        seen = {start} | set(deadends)

        while queue:
            cur_node, depth = queue.popleft()
            if cur_node == target:
                return depth
            for i in range(n):
                for digit in self.NEIGHBOURS[cur_node[i]]:
                    new_node = cur_node[:i] + digit + cur_node[i + 1:]
                    if new_node not in seen:
                        seen.add(new_node)
                        queue.append((new_node, depth + 1))

        return -1
