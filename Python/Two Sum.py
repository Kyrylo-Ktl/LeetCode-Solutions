from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(numbers):
            if target - num in index:
                return [index[target - num], i]
            index[num] = i
