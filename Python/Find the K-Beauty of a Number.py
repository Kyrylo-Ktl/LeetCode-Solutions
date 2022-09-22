class Solution:
    """
    Time:   O(log10(n)*k)
    Memory: O(k)
    """

    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        return sum(
            num % int(str_num[i - k:i]) == 0
            for i in range(k, len(str_num) + 1)
            if int(str_num[i - k:i]) != 0
        )


class Solution:
    """
    Time:   O(log10(n))
    Memory: O(1)
    """

    def divisorSubstrings(self, num: int, k: int) -> int:
        power = 10 ** (k - 1)
        tmp, window = divmod(num, 10 * power)

        count = int(window and not num % window)
        while tmp:
            tmp, digit = divmod(tmp, 10)
            window = digit * power + window // 10
            count += window and not num % window

        return count
