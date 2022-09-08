from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(area, max_area)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
