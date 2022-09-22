class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def reverseWords(self, string: str) -> str:
        return ' '.join(word[::-1] for word in string.split())

