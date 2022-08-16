from collections import Counter


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def firstUniqChar(self, string: str) -> int:
        count = Counter(string)

        for i, ch in enumerate(string):
            if count[ch] == 1:
                return i

        return -1
