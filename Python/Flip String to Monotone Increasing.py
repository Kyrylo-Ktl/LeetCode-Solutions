class Solution:
    """
    Time:   O(n)
    Memory: O(1)
    """

    def minFlipsMonoIncr(self, s: str) -> int:
        ones = flip = 0

        for ch in s:
            if ch == '1':
                ones += 1
            else:
                flip += 1
            flip = min(ones, flip)

        return flip
