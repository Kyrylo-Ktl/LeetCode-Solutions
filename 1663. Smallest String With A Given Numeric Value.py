class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def getSmallestString(self, n: int, k: int) -> str:
        s = [ord('a')] * n

        k = k - n
        for i in reversed(range(n)):
            if k < 25:
                s[i] += k
                break
            s[i] += 25
            k -= 25

        return ''.join(map(chr, s))
