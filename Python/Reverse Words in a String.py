class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
