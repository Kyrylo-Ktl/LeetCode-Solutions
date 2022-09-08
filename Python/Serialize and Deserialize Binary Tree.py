from typing import Iterator, Generator, Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    """
    Time:   O(n)
    Memory: O(n)
    """

    DELIMITER = ' '
    END = '#'

    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.DELIMITER.join(self._preorder(root))

    @classmethod
    def _preorder(cls, node: Optional[TreeNode]) -> Generator:
        if node is None:
            yield cls.END
        else:
            yield str(node.val)
            yield from cls._preorder(node.left)
            yield from cls._preorder(node.right)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        return self._deserialize(iter(data.split(self.DELIMITER)))

    @classmethod
    def _deserialize(cls, preorder: Iterator) -> Optional[TreeNode]:
        val = next(preorder)
        return TreeNode(
            int(val),
            cls._deserialize(preorder),
            cls._deserialize(preorder),
        ) if val != cls.END else None
