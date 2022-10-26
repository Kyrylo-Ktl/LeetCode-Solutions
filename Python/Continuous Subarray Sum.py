from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}
        s = 0

        for i, num in enumerate(nums):
            s += num
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True

        return False
