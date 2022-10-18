from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = set(arr)
        for num in range(1, k + len(arr) + 1):
            if num not in seen:
                k -= 1
            if not k:
                return num
