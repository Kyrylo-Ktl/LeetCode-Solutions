from typing import List


class Solution:
    """
    Time:   O(n^2*k^2)
    Memory: O(1)

    where k - the longest word length
    """

    def stringMatching(self, words: List[str]) -> List[str]:
        words = sorted(words, key=len)
        result = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break

        return result
