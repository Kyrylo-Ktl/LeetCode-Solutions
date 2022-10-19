class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        i = 0

        while left != right:
            left >>= 1
            right >>= 1
            i += 1

        return left << i
