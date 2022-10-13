from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(n*k)
    Memory: O(k)

    where k - the longest word length
    """

    def removeAnagrams(self, words: List[str]) -> List[str]:
        prev = Counter()
        result = []

        for word in words:
            curr = Counter(word)
            if prev != curr:
                prev = Counter(word)
                result.append(word)

        return result
