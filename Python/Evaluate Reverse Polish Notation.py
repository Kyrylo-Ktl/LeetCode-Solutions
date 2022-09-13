from typing import List


class Solution:
    """
    Time:   O(n)
    Memory: O(n)
    """

    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    def evalRPN(self, tokens: List[int]) -> int:
        stack = []

        for token in tokens:
            if token in self.OPERATORS:
                a, b = stack.pop(), stack.pop()
                stack.append(self.OPERATORS[token](a, b))
            else:
                stack.append(int(token))

        return stack.pop()
