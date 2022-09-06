from collections import Counter, defaultdict


class Solution:
    """
    Time:   O(max(n,m))
    Memory: O(n+m)
    """

    def isAnagram(self, first: str, second: str) -> bool:
        return Counter(first) == Counter(second)


class Solution:
    """
    Time:   O(max(n,m))
    Memory: O(max(n,m))
    """

    def isAnagram(self, first: str, second: str) -> bool:
        counter = defaultdict(int)

        if len(first) != len(second):
            return False

        for char in first:
            counter[char] += 1

        for char in second:
            if char not in counter:
                return False
            counter[char] -= 1

        return not any(counter.values())
