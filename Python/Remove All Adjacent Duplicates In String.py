class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def removeDuplicates(self, string: str) -> str:
        stack = []

        for c in string:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
