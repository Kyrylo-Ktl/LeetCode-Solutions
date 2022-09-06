class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minSteps(self, s: str, t: str) -> int:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        for char in t:
            count[ord(char) - ord('a')] -= 1

        return sum(val for val in count if val > 0)
