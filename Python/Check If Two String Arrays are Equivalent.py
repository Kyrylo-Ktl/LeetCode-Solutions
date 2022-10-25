from typing import Generator, List
from itertools import zip_longest


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def arrayStringsAreEqual(self, a: List[str], b: List[str]) -> bool:
        return ''.join(a) == ''.join(b)


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def arrayStringsAreEqual(self, a: List[str], b: List[str]) -> bool:
        for i, j in zip_longest(self._stream_letters(a), self._stream_letters(b), fillvalue=None):
            if i != j:
                return False
        return True

    @staticmethod
    def _stream_letters(words: List[str]) -> Generator:
        for word in words:
            yield from word
