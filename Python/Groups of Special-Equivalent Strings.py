from typing import List


class Solution:
    """
    Time:   O(n*k*log(k))
    Memory: O(n*k)

    where k - maximum word length
    """

    def numSpecialEquivGroups(self, words: List[str]) -> int:
        return len({
            (
                ''.join(sorted(word[::2])),
                ''.join(sorted(word[1::2])),
            )
            for word in words
        })
