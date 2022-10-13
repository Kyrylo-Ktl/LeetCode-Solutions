class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def getLucky(self, s: str, k: int) -> int:
        num = self.to_number(s)

        while k > 0 and num >= 10:
            num = self.sum_digits(num)
            k -= 1

        return num

    @staticmethod
    def to_number(s: str) -> int:
        return int(''.join(str(ord(c) - ord('a') + 1) for c in s))

    @staticmethod
    def sum_digits(num: int) -> int:
        return sum(int(d) for d in str(num))
