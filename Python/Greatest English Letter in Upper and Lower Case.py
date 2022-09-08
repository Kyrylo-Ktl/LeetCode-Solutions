class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def greatestLetter(self, s: str) -> str:
        letters = set(s)

        for ltr in sorted(letters, reverse=True):
            if ltr.isupper() and ltr.lower() in letters:
                return ltr

        return ''


class Solution:
    """
    Time:   O(2*26)
    Memory: O(2*26)
    """

    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        greatest = ''

        for ltr in letters:
            if ltr.isupper() and ltr.lower() in letters:
                greatest = max(ltr, greatest)

        return greatest
