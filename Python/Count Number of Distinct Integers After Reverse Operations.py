from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def countDistinctIntegers(self, nums: List[int]) -> int:
        uniq = set()

        for num in nums:
            uniq.add(num)
            uniq.add(int(str(num)[::-1]))

        return len(uniq)
