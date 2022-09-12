from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to, trusted = [0] * n, [0] * n

        for u, v in trust:
            trust_to[u - 1] += 1
            trusted[v - 1] += 1

        for town, (tr, tr_to) in enumerate(zip(trusted, trust_to), start=1):
            if tr_to == 0 and tr == n - 1:
                return town

        return -1
