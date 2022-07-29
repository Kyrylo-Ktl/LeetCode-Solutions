from typing import List


class Solution:
    """
    Time:   O(n*k)
    Memory: O(k)

    k - length of each word
    n - length of pattern
    """

    def findAndReplacePattern(self, words: List[str], pattern: str):
        def match(word: str) -> bool:
            mapping = {}

            for x, y in zip(pattern, word):
                if mapping.setdefault(x, y) != y:
                    return False

            return len(set(mapping.values())) == len(mapping.values())

        return filter(match, words)
