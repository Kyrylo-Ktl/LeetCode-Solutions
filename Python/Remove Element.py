from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        for num in nums:
            if num == val:
                continue
            nums[i] = num
            i += 1

        return i
