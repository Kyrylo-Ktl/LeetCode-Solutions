from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Time:   O(n)
    Memory: O(log(n))
    """

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self._construct(0, len(nums) - 1, nums)

    @classmethod
    def _construct(cls, left: int, right: int, nums: List[int]) -> Optional[TreeNode]:
        if left <= right:
            mid = (left + right) // 2
            return TreeNode(
                val=nums[mid],
                left=cls._construct(left, mid - 1, nums),
                right=cls._construct(mid + 1, right, nums),
            )
