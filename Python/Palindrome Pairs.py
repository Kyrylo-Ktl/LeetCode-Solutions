from typing import List, Set, Tuple


class Solution:
    """
    Time:   O(n*k^2)
    Memory: O(n)

    where k - max string length in words
    """

    def palindromePairs(self, words: List[str]) -> Set[Tuple[int, int]]:
        index = {w: i for i, w in enumerate(words)}
        pairs = set()

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                inv_prefix, inv_suffix = prefix[::-1], suffix[::-1]

                if prefix == inv_prefix and index.get(inv_suffix, i) != i:
                    pairs.add((index[inv_suffix], i))

                if suffix == inv_suffix and index.get(inv_prefix, i) != i:
                    pairs.add((i, index[inv_prefix]))

        return pairs
