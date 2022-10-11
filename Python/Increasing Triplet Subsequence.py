from sys import maxsize
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def increasingTriplet(self, nums: List[int]) -> bool:
        first_min = second_min = maxsize

        for num in nums:
            if num <= first_min:
                first_min = num
            elif num <= second_min:
                second_min = num
            else:
                return True

        return False
