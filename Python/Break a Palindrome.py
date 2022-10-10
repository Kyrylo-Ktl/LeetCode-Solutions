class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''

        n = len(palindrome)
        letters = list(palindrome)

        for i in range(n // 2):
            if letters[i] > 'a':
                letters[i] = 'a'
                break
        else:
            letters[-1] = 'b'

        return ''.join(letters)
