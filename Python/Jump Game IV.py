from collections import defaultdict, deque
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        duplicates = defaultdict(list)
        for i, num in enumerate(arr):
            duplicates[num].append(i)

        queue = deque([(0, 0)])
        visited, visited_groups = set(), set()

        while queue:
            i, steps = queue.popleft()

            if i == n - 1:
                return steps

            for j in (i - 1, i + 1):
                if 0 <= j < n and j not in visited and arr[j] not in visited_groups:
                    visited.add(j)
                    queue.append((j, steps + 1))

            if arr[i] in visited_groups:
                continue

            for j in duplicates[arr[i]]:
                if j not in visited:
                    visited.add(j)
                    queue.append((j, steps + 1))

            visited_groups.add(arr[i])

        return -1
