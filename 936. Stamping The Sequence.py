from typing import List


class Solution:
    """
    Time:   O(m*(m-n))
    Memory: O(m*(m-n))

    n - length of stamp
    m - length of target
    """

    MASK = '?'

    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        target = list(target)
        m, n = len(target), len(stamp)
        ans = []
        seen = set()

        for i in range(m - n + 1):
            if not self.equals(stamp, target, i):
                continue

            for j in reversed(range(i + 1)):
                if j in seen:
                    break

                seen.add(j)
                if self.equals(stamp, target, j):
                    ans.append(j)
                    target[j:j + n] = [self.MASK] * n

        return ans[::-1] if target == [self.MASK] * m else []

    @classmethod
    def equals(cls, stamp: str, target: list, i: int) -> bool:
        for j, c in enumerate(stamp):
            if target[i + j] not in (c, cls.MASK):
                return False
        return True
