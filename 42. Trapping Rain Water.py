from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def trap(self, height: List[int]) -> int:
        n = len(height)

        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max = [0] * n
        right_max[-1] = height[-1]
        for i in reversed(range(0, n - 1)):
            right_max[i] = max(height[i], right_max[i + 1])

        return sum(min(l_max, r_max) - h for h, l_max, r_max in zip(height, left_max, right_max))
