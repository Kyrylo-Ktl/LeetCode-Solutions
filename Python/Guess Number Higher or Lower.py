class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            pick = guess(mid)

            if pick == 0:
                return mid

            if pick < 0:
                right = mid - 1
            else:
                left = mid + 1

        return -1
