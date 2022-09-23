from itertools import zip_longest


class Solution:
    """
    Time:   O(max(n,m))
    Memory: O(n+m)
    """

    def compareVersion(self, version1: str, version2: str) -> int:
        for v1, v2 in zip_longest(
                map(int, version1.split('.')),
                map(int, version2.split('.')),
                fillvalue=0
        ):
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1

        return 0
