class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def removeStars(self, string: str) -> str:
        stack = []

        for c in string:
            if c == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
