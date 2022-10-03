from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minCost(self, colors: str, needed_time: List[int]) -> int:
        total_cost = color_cost = max_color_cost = 0
        prev_color = '*'

        for color, time in zip(colors, needed_time):
            if color == prev_color:
                color_cost += time
                max_color_cost = max(max_color_cost, time)
            else:
                total_cost += color_cost - max_color_cost
                color_cost = max_color_cost = time
                prev_color = color

        return total_cost + (color_cost - max_color_cost)
