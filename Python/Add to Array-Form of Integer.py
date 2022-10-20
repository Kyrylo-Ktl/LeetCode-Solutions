from typing import List


class Solution:
    """
    Time:   O(log10(k))
    Memory: O(1)
    """

    BASE = 10

    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i = len(num) - 1

        while i >= 0 and k:
            k, num[i] = divmod(num[i] + k, self.BASE)
            i -= 1

        while k:
            k, a = divmod(k, self.BASE)
            num.insert(0, a)

        return num
