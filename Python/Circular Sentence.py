class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        return all(words[i][-1] == words[(i + 1) % n][0] for i in range(n))


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def isCircularSentence(self, sentence: str) -> bool:
        for i, c in enumerate(sentence):
            if c == ' ' and sentence[i - 1] != sentence[i + 1]:
                return False
        return sentence[0] == sentence[-1]
