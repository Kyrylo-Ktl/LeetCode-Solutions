from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(k)
    """

    K = 2

    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        max_fruits = i = 0

        for j, tree in enumerate(fruits):
            window[tree] += 1

            while len(window) > self.K:
                window[fruits[i]] -= 1
                if not window[fruits[i]]:
                    window.pop(fruits[i])
                i += 1

            max_fruits = max(max_fruits, j - i + 1)

        return max_fruits
