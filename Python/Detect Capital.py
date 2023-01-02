class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
