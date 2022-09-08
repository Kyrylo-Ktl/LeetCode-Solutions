from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = sum(cnt // 2 for cnt in Counter(nums).values())
        return [pairs, len(nums) - 2 * pairs]


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs = 0
        single = set()

        for num in nums:
            if num in single:
                single.remove(num)
                pairs += 1
            else:
                single.add(num)

        return [pairs, len(single)]
