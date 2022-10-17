class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
