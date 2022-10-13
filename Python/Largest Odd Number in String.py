class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        for i in reversed(range(n)):
            if int(num[i]) & 1:
                return num[:i + 1]

        return ''
