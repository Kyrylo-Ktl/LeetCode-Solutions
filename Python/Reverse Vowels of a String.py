class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    VOWELS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def reverseVowels(self, string: str) -> str:
        letters = list(string)
        left, right = 0, len(string) - 1

        while left < right:
            if letters[left] in self.VOWELS and letters[right] in self.VOWELS:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
            if letters[left] not in self.VOWELS:
                left += 1
            if letters[right] not in self.VOWELS:
                right -= 1

        return ''.join(letters)
