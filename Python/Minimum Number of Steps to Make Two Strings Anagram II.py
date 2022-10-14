from collections import Counter


class Solution:
    """
    Time:   O(n+m)
    Memory: O(n+m)
    """

    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        return sum((s_cnt - t_cnt).values()) + sum((t_cnt - s_cnt).values())
