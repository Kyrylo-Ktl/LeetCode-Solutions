import collections
import heapq
from typing import List


class Solution:
    """
    Time:   O(n*log(n))
    Memory: O(n)
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = collections.Counter(words)
        return heapq.nsmallest(k, freq, key=lambda word: (-freq[word], word))
