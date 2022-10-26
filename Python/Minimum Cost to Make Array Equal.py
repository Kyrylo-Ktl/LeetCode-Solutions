from typing import List


class Solution:
    """
    Time:   O(n*log(m))
    Memory: O(1)

    where m - range of values, i.e. maximum - minimum
    """

    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def cost_function(x: int) -> int:
            return sum(abs(n - x) * c for n, c in zip(nums, cost))

        left, right = min(nums), max(nums)
        min_cost = cost_function(left)

        while left < right:
            mid = (left + right) // 2
            y1, y2 = cost_function(mid), cost_function(mid + 1)
            min_cost = min(y1, y2)

            if y1 < y2:
                right = mid
            else:
                left = mid + 1

        return min_cost
