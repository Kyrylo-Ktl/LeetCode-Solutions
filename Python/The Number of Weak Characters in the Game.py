from itertools import groupby
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True)
        max_defence = weak = 0

        for _, group in groupby(properties, key=lambda x: x[0]):
            defences = [d for _, d in group]
            weak += sum(d < max_defence for d in defences)
            max_defence = max(max_defence, max(defences))

        return weak
