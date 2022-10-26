class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    MOD = 10 ** 9 + 7

    def numSub(self, s: str) -> int:
        num = ones = 0

        for c in s:
            ones = ones + 1 if c == '1' else 0
            num = (num + ones) % self.MOD

        return num
