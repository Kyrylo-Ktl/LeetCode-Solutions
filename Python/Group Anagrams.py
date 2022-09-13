from collections import defaultdict
from typing import List


class Solution:
    """
    Time:   O(n*m*log(m))
    Memory: O(n*m)

    where m - max string length
    """

    def groupAnagrams(self, string: List[str]):
        anagrams = defaultdict(list)

        for s in string:
            anagrams[''.join(sorted(s))].append(s)

        return anagrams.values()
