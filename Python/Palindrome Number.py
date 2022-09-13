class Solution:
    """
    Time:   O(log10(n))
    Memory: O(log10(n))
    """

    def isPalindrome(self, num: int) -> bool:
        digits = str(num)
        for i in range(len(digits) // 2):
            if digits[i] != digits[len(digits) - i - 1]:
                return False
        return True


class Solution:
    """
    Time:   O(log10(n))
    Memory: O(1)
    """

    def isPalindrome(self, num: int) -> bool:
        if num < 0 or (not num % 10 and num):
            return False

        reverted = 0
        while num > reverted:
            num, digit = divmod(num, 10)
            reverted = reverted * 10 + digit

        return num == reverted or num == reverted // 10
