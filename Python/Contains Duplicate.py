from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
