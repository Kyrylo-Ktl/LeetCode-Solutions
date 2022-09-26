from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _, name in sorted(zip(heights, names), reverse=True)]
