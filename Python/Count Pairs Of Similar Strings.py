from collections import Counter
from functools import reduce
from operator import or_
from typing import List


class Solution:
    """
    Time:   O(n^2*m)
    Memory: O(m)

    where m - maximum word length
    """

    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        return sum(set(words[i]) == set(words[j]) for i in range(n) for j in range(i + 1, n))


class Solution:
    """
    Time:   O(n^2*m)
    Memory: O(1)

    where m - maximum word length
    """

    def similarPairs(self, words: List[str]) -> int:
        n = len(words)
        return sum(
            self.strint_to_bitmask(words[i]) == self.strint_to_bitmask(words[j])
            for i in range(n)
            for j in range(i + 1, n)
        )

    @staticmethod
    def strint_to_bitmask(string: str) -> int:
        return reduce(or_, (1 << (ord(c) - ord('a')) for c in string), 0)


class Solution:
    """
    Time:   O(n*m)
    Memory: O(n)

    where m - maximum word length
    """

    def similarPairs(self, words: List[str]) -> int:
        frequency = Counter(map(self.strint_to_bitmask, words))
        return sum(f * (f - 1) // 2 for f in frequency.values())

    @staticmethod
    def strint_to_bitmask(string: str) -> int:
        return reduce(or_, (1 << (ord(c) - ord('a')) for c in string), 0)
