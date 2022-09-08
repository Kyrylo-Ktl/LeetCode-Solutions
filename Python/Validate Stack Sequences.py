from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []

        for i in pushed:
            stack.append(i)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.pop(0)

        return not stack
