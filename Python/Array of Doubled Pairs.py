from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n + k*log2(k))
    Memory: O(n)
    """

    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = Counter(arr)

        for num in sorted(count, key=abs):
            if count[num] > count[2 * num]:
                return False
            count[2 * num] -= count[num]

        return True
