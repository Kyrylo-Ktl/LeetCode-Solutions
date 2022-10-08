from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def distributeCandies(self, candy_types: List[int]) -> int:
        unique_candies = len(set(candy_types))
        return min(unique_candies, len(candy_types) // 2)
