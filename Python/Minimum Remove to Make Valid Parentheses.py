class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    def minRemoveToMakeValid(self, s):
        stack = []
        chars = list(s)

        for i, ch in enumerate(chars):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    chars[i] = ''

        for i in stack:
            chars[i] = ''

        return ''.join(chars)
