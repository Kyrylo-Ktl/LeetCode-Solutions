from string import ascii_lowercase


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkIfPangram(self, sentence: str) -> bool:
        for c in ascii_lowercase:
            if c not in sentence:
                return False
        return True


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26

        for c in sentence:
            seen[ord(c) - ord('a')] = True

        for status in seen:
            if not status:
                return False

        return True


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def checkIfPangram(self, sentence: str) -> bool:
        seen = 0

        for c in sentence:
            seen |= 1 << ord(c) - ord('a')

        return seen == (1 << 26) - 1
