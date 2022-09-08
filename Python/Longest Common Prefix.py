from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        prefix = ''

        for ind, sym in enumerate(min_str):
            for other in strs:
                if other[ind] != sym:
                    return prefix
            prefix += sym

        return prefix
