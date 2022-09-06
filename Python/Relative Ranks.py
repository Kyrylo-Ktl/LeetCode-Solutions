from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    MEDALS = {
        1: 'Gold Medal',
        2: 'Silver Medal',
        3: 'Bronze Medal',
    }

    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ranks = {num: ind for ind, num in enumerate(sorted(nums, reverse=True), start=1)}
        return [self._get_place(ranks[num]) for num in nums]

    @classmethod
    def _get_place(cls, place: int) -> str:
        return cls.MEDALS.get(place, str(place))
