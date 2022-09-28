from typing import List


class Solution:
    """
    Time:   O(n*k^2)
    Memory: O(n)

    where k - max word length
    """

    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        memo = {w: 1 for w in words}

        for word in words:
            for j in range(len(word)):
                memo[word] = max(memo[word], 1 + memo.get(word[:j] + word[j + 1:], 0))

        return max(memo.values())
