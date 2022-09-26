class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def wordPattern(self, pattern: str, string: str) -> bool:
        words = string.split()

        if len(words) != len(pattern):
            return False

        pattern_map = {}
        string_map = {}

        for p, w in zip(pattern, words):
            if pattern_map.setdefault(p, w) != w or string_map.setdefault(w, p) != p:
                return False

        return True
