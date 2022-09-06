from collections import deque
from typing import List


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

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        level = (root,)
        while level:
            yield sum(node.val for node in level) / len(level)
            level = (
                child
                for node in level
                for child in (node.left, node.right)
                if child is not None
            )


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque([root])
        averages = []

        while queue:
            level_sum = level_cnt = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node is not None:
                    level_sum += node.val
                    level_cnt += 1
                    queue.append(node.left)
                    queue.append(node.right)
            if level_cnt:
                averages.append(level_sum / level_cnt)

        return averages
