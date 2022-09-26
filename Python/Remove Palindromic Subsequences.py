class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def removePalindromeSub(self, s: str) -> int:
        return 1 + (s != s[::-1])


class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def removePalindromeSub(self, s: str) -> int:
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return 2
        return 1
