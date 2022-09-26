class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def validPalindrome(self, string: str) -> bool:
        for i in range(len(string)):
            j = len(string) - 1 - i
            if string[i] != string[j]:
                return self.is_palindrome(string, i, j - 1) or self.is_palindrome(string, i + 1, j)
        return True

    @staticmethod
    def is_palindrome(string: str, start: int, end: int) -> bool:
        for i in range((end - start + 1) // 2):
            if string[start + i] != string[end - i]:
                return False
        return True


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def validPalindrome(self, string: str) -> bool:
        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return self.is_palindrome(string, i, j - 1) or \
                       self.is_palindrome(string, i + 1, j)
            i += 1
            j -= 1

        return True

    @staticmethod
    def is_palindrome(string: str, start: int, end: int) -> bool:
        for i in range((end - start + 1) // 2):
            if string[start + i] != string[end - i]:
                return False
        return True
