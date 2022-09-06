from collections import Counter


class Solution:
    """
    Time:   O(1)
    Memory: O(1)
    """

    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        palindrome = mid = ''

        for d in sorted(count.keys(), reverse=True):
            mid = max(mid, d * (count[d] & 1))
            palindrome += d * (count[d] // 2)

        palindrome = palindrome.lstrip('0')
        return (palindrome + mid + palindrome[::-1]) or '0'
