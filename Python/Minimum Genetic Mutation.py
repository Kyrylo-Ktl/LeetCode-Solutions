from collections import deque
from typing import List, Generator


class Solution:
    """
    Time:   O(n*m^2)
    Memory: O(n)

    where m - gen length
    """

    GENS = 'ACGT'

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue = deque([(start, 0)])
        seen = {start}

        while queue:
            curr, steps = queue.popleft()

            if curr == end:
                return steps

            for neighbor in self.get_mutations(curr):
                if neighbor in bank and neighbor not in seen:
                    queue.append((neighbor, steps + 1))
                    seen.add(neighbor)

        return -1

    @classmethod
    def get_mutations(cls, gen: str) -> Generator:
        for i in range(len(gen)):
            for c in cls.GENS:
                yield gen[:i] + c + gen[i + 1:]
