class Solution:
    """
    Time:   O(log(n))
    Memory: O(1)
    """

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) >> 1
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
