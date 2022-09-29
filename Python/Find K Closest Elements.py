from bisect import bisect
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr, key=lambda i: abs(x - i))[:k])


class Solution:
    """
    Time:   O(log(n) + k)
    Memory: O(1)
    """

    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        j = bisect(nums, x)
        i = j - 1

        for _ in range(k):
            if j >= len(nums) or (i >= 0 and abs(nums[i] - x) <= abs(nums[j] - x)):
                i -= 1
            else:
                j += 1

        return nums[i + 1:j]
