class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def makeGood(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c.swapcase() == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
