from typing import List


class Solution:
    """
    Time:   O(N + M)
    Memory: O(1)

    where N - max 'x' value,
          M - max 'y' value
    """

    def findSolution(self, custom_function: 'CustomFunction', z: int) -> List[List[int]]:
        x, y = 1, z
        pairs = []

        while x <= z and y > 0:
            val = custom_function.f(x, y)
            if val == z:
                pairs.append([x, y])
            if val >= z:
                y -= 1
            if val <= z:
                x += 1

        return pairs
