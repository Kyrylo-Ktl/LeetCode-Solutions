from collections import Counter
from typing import List


class Solution:
    """
    Time:   O(m*max(n,k))
    Memory: O(n+k)

    n - length of letters in license_plate
    m - length of words
    k - length of each word in words
    """

    def shortestCompletingWord(self, license_plate: str, words: List[str]) -> str:
        letters = Counter(ltr.lower() for ltr in license_plate if ltr.isalpha())
        return min((word for word in words if not letters - Counter(word)), key=len)
