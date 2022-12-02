from collections import Counter


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def closeStrings(self, a: str, b: str) -> bool:
        a_cnt, b_cnt = Counter(a), Counter(b)
        return a_cnt.keys() == b_cnt.keys() and sorted(a_cnt.values()) == sorted(b_cnt.values())
