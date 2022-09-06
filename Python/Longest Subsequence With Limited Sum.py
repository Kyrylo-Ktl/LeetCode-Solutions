from bisect import bisect
from itertools import accumulate
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        cumsum = list(accumulate(sorted(nums)))
        return [bisect(cumsum, q) for q in queries]
