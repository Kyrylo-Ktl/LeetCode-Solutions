from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index = {}

        for i, num in enumerate(nums):
            if num in index and i - index[num] <= k:
                return True
            index[num] = i

        return False
